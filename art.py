#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spin Shapes (Cube / Pyramid) — pygame
=====================================
A tiny, dependency-light 3D demo that renders a spinning cube or pyramid with
perspective projection. Non-ASCII graphics (uses an actual window).

Controls
--------
  SPACE        Toggle auto-rotate on/off
  C            Switch to Cube
  P            Switch to Pyramid
  W/S          Pitch up/down
  A/D          Yaw left/right
  Q/E          Roll left/right
  Z/X          Zoom in/out
  R            Reset rotation/zoom
  F            Toggle filled faces vs wireframe
  B            Toggle backface culling when filled
  T            Toggle face translucency (alpha)
  Arrow Keys   Nudge rotation (fine control)
  Mouse drag   Rotate (hold left button and move)
  Mouse wheel  Zoom in/out
  Esc/Close    Quit

Config (edit below)
-------------------
You can tweak SHAPE, WINDOW size, colors, rotation speed, etc. directly in the
CONFIG section near the top of the file.
"""
import math
import sys
from dataclasses import dataclass
from typing import List, Tuple

import pygame

# ---------------------- CONFIG ----------------------
SHAPE = "cube"             # "cube" or "pyramid"
WINDOW = (900, 650)        # width, height
BG_COLOR = (12, 14, 20)    # background color
EDGE_COLOR = (230, 230, 235)
FACE_COLORS = [            # RGBA tuples for faces when filled=True
    (255, 120, 120, 180),
    (120, 255, 120, 180),
    (120, 160, 255, 180),
    (255, 220, 120, 180),
    (220, 120, 255, 180),
    (120, 255, 220, 180),
]
EDGE_THICKNESS = 2
FOV_DEG = 70               # field of view (perspective)
NEAR, FAR = 0.1, 100.0

AUTO_ROTATE = True
ROT_SPEED = (0.6, 0.9, 0.3)  # radians/sec around (x, y, z)
ZOOM = 2.2                    # scene scale multiplier
FILLED = True                 # draw filled faces
BACKFACE_CULL = True          # cull faces facing away from camera
ALPHA = True                  # use per-face alpha
# ----------------------------------------------------

Vec3 = Tuple[float, float, float]

@dataclass
class Mesh:
    vertices: List[Vec3]
    faces: List[Tuple[int, int, int, int]]  # quads; triangles repeat one index

def make_cube(size: float=1.2) -> Mesh:
    s = size / 2.0
    v = [
        (-s, -s, -s), ( s, -s, -s), ( s,  s, -s), (-s,  s, -s),  # back  (z=-s)
        (-s, -s,  s), ( s, -s,  s), ( s,  s,  s), (-s,  s,  s),  # front (z= s)
    ]
    f = [
        (0, 1, 2, 3),  # back
        (4, 5, 6, 7),  # front
        (0, 1, 5, 4),  # bottom
        (2, 3, 7, 6),  # top
        (1, 2, 6, 5),  # right
        (0, 3, 7, 4),  # left
    ]
    return Mesh(v, f)

def make_pyramid(size: float=1.6, height: float=1.8) -> Mesh:
    s = size / 2.0
    v = [
        (-s, -s, 0.0), ( s, -s, 0.0), ( s,  s, 0.0), (-s,  s, 0.0),  # base (z=0)
        (0.0, 0.0, height),  # apex
    ]
    # Represent triangles as quads with repeated last index
    f = [
        (0, 1, 2, 3),   # base
        (0, 1, 4, 4),   # sides:
        (1, 2, 4, 4),
        (2, 3, 4, 4),
        (3, 0, 4, 4),
    ]
    return Mesh(v, f)

def rotate_x(p: Vec3, a: float) -> Vec3:
    x, y, z = p
    ca, sa = math.cos(a), math.sin(a)
    return (x, y*ca - z*sa, y*sa + z*ca)

def rotate_y(p: Vec3, a: float) -> Vec3:
    x, y, z = p
    ca, sa = math.cos(a), math.sin(a)
    return (x*ca + z*sa, y, -x*sa + z*ca)

def rotate_z(p: Vec3, a: float) -> Vec3:
    x, y, z = p
    ca, sa = math.cos(a), math.sin(a)
    return (x*ca - y*sa, x*sa + y*ca, z)

def add(p: Vec3, q: Vec3) -> Vec3:
    return (p[0]+q[0], p[1]+q[1], p[2]+q[2])

def sub(p: Vec3, q: Vec3) -> Vec3:
    return (p[0]-q[0], p[1]-q[1], p[2]-q[2])

def cross(a: Vec3, b: Vec3) -> Vec3:
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def dot(a: Vec3, b: Vec3) -> float:
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def length(a: Vec3) -> float:
    return math.sqrt(dot(a, a))

def normalize(a: Vec3) -> Vec3:
    l = length(a) or 1.0
    return (a[0]/l, a[1]/l, a[2]/l)

def project(v: Vec3, fov_deg: float, width: int, height: int, zoom: float) -> Tuple[int, int, float]:
    """
    Simple perspective projection.
    Returns (screen_x, screen_y, depth_z) where depth_z is positive in front of camera.
    Camera at origin looking down +Z, with right-handed coords.
    """
    f = 1.0 / math.tan(math.radians(fov_deg)/2.0)
    x, y, z = v
    z = z if z > 1e-4 else 1e-4
    px = (x * f / z) * zoom
    py = (y * f / z) * zoom
    sx = int((px * width/2) + width/2)
    sy = int((-py * height/2) + height/2)
    return sx, sy, z

def face_normal(v0: Vec3, v1: Vec3, v2: Vec3) -> Vec3:
    return normalize(cross(sub(v1, v0), sub(v2, v0)))

def avg_depth(pts: List[Vec3]) -> float:
    return sum(p[2] for p in pts) / max(1, len(pts))

def shape_mesh(name: str) -> Mesh:
    n = name.lower().strip()
    if n == "cube":
        return make_cube(1.2)
    if n == "pyramid":
        return make_pyramid(1.6, 1.8)
    raise ValueError("Unknown shape: %r" % name)

def main():
    pygame.init()
    pygame.display.set_caption("Spin Shapes — Cube / Pyramid (pygame)")
    screen = pygame.display.set_mode(WINDOW, pygame.SRCALPHA, 32)
    clock = pygame.time.Clock()

    # Scene state
    mesh = shape_mesh(SHAPE)
    filled = FILLED
    backface_cull = BACKFACE_CULL
    use_alpha = ALPHA

    # Object transform: centered at origin, translated forward on +Z
    obj_rot = [0.0, 0.0, 0.0]  # rx, ry, rz in radians
    obj_pos = (0.0, 0.0, 5.0)  # move 5 units forward
    zoom = ZOOM
    auto_rotate = AUTO_ROTATE

    dragging = False
    last_mouse = (0, 0)

    def transform_world(v: Vec3) -> Vec3:
        # Apply object rotation, then translation
        x = rotate_x(v, obj_rot[0])
        y = rotate_y(x, obj_rot[1])
        z = rotate_z(y, obj_rot[2])
        return add(z, obj_pos)

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    auto_rotate = not auto_rotate
                elif event.key == pygame.K_c:
                    mesh = shape_mesh("cube")
                elif event.key == pygame.K_p:
                    mesh = shape_mesh("pyramid")
                elif event.key == pygame.K_f:
                    filled = not filled
                elif event.key == pygame.K_b:
                    backface_cull = not backface_cull
                elif event.key == pygame.K_t:
                    use_alpha = not use_alpha
                elif event.key == pygame.K_r:
                    obj_rot[:] = [0.0, 0.0, 0.0]
                    zoom = ZOOM
                elif event.key == pygame.K_z:
                    zoom *= 1.1
                elif event.key == pygame.K_x:
                    zoom /= 1.1
                elif event.key == pygame.K_w:
                    obj_rot[0] -= 0.15
                elif event.key == pygame.K_s:
                    obj_rot[0] += 0.15
                elif event.key == pygame.K_a:
                    obj_rot[1] -= 0.15
                elif event.key == pygame.K_d:
                    obj_rot[1] += 0.15
                elif event.key == pygame.K_q:
                    obj_rot[2] -= 0.15
                elif event.key == pygame.K_e:
                    obj_rot[2] += 0.15
                elif event.key == pygame.K_UP:
                    obj_rot[0] -= 0.05
                elif event.key == pygame.K_DOWN:
                    obj_rot[0] += 0.05
                elif event.key == pygame.K_LEFT:
                    obj_rot[1] -= 0.05
                elif event.key == pygame.K_RIGHT:
                    obj_rot[1] += 0.05
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    last_mouse = event.pos
                elif event.button == 4:  # wheel up
                    zoom *= 1.08
                elif event.button == 5:  # wheel down
                    zoom /= 1.08
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
            elif event.type == pygame.MOUSEMOTION and dragging:
                x, y = event.pos
                lx, ly = last_mouse
                dx, dy = x - lx, y - ly
                last_mouse = (x, y)
                # Drag rotates around y (dx) and x (dy)
                obj_rot[1] += dx * 0.01
                obj_rot[0] += dy * 0.01

        if auto_rotate:
            obj_rot[0] += ROT_SPEED[0] * dt
            obj_rot[1] += ROT_SPEED[1] * dt
            obj_rot[2] += ROT_SPEED[2] * dt

        screen.fill(BG_COLOR)

        # Transform vertices to world space, then project
        wverts: List[Vec3] = [transform_world(v) for v in mesh.vertices]
        sverts = [project(v, FOV_DEG, screen.get_width(), screen.get_height(), zoom) for v in wverts]

        # Build face draw list with depth sorting (painter's algorithm)
        draw_faces = []
        for i, face in enumerate(mesh.faces):
            idx = list(face)
            v0, v1, v2, v3 = [wverts[j] for j in idx]
            # normal for backface culling (use first triangle of the quad)
            n = face_normal(v0, v1, v2)
            center = ((v0[0]+v1[0]+v2[0]+v3[0])/4.0,
                      (v0[1]+v1[1]+v2[1]+v3[1])/4.0,
                      (v0[2]+v1[2]+v2[2]+v3[2])/4.0)
            view = normalize((0.0-center[0], 0.0-center[1], 0.0-center[2]))  # towards camera at origin
            facing = dot(n, view) > 0.0
            depth = avg_depth([v0, v1, v2, v3])
            draw_faces.append((depth, i, idx, facing))

        # Back to front for painter's algorithm
        draw_faces.sort(key=lambda x: x[0], reverse=True)

        # Draw faces + edges
        for _, i, idx, facing in draw_faces:
            color = FACE_COLORS[i % len(FACE_COLORS)]
            points_2d = [(sverts[j][0], sverts[j][1]) for j in idx]

            if filled:
                if not backface_cull or facing:
                    if ALPHA and len(color) == 4:
                        surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
                        pygame.draw.polygon(surf, color, points_2d)
                        screen.blit(surf, (0, 0))
                    else:
                        pygame.draw.polygon(screen, color[:3], points_2d)

            # wireframe edges on top
            for a, b in zip(idx, idx[1:]+idx[:1]):
                pygame.draw.line(screen, EDGE_COLOR,
                                 (sverts[a][0], sverts[a][1]),
                                 (sverts[b][0], sverts[b][1]),
                                 EDGE_THICKNESS)

        # HUD text
        font = pygame.font.SysFont("consolas,dejavusansmono,monospace", 16)
        hud_lines = [
            f"[{SHAPE.upper()}] AutoRotate:{auto_rotate}  Filled:{filled}  Cull:{backface_cull}  Alpha:{ALPHA}  Zoom:{zoom:.2f}",
            "Keys: SPACE auto | C cube | P pyramid | F fill | B cull | T alpha | R reset | Z/X zoom | WASD/QE rotate | Arrows fine | Mouse drag+wheel",
        ]
        y = 8
        for line in hud_lines:
            text = font.render(line, True, (220, 220, 235))
            screen.blit(text, (10, y))
            y += 20

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        raise
