import pygame
import sys
import random

# --- Settings ---
WIDTH, HEIGHT = 600, 400
PADDLE_W, PADDLE_H = 100, 15
BALL_R = 10
OBSTACLE_R = 40
HELP_BALL_R = 25
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong")
clock = pygame.time.Clock()

# Paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, HEIGHT - 40, PADDLE_W, PADDLE_H)

# Obstacle
obstacle = pygame.Rect(WIDTH // 2, HEIGHT // 2, OBSTACLE_R*2, OBSTACLE_R*2)
obstacle_speed = [0, -3]
obstacle.top = 0

# Help ball
help_ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, HELP_BALL_R*2, HELP_BALL_R*2)
help_active = False
help_fall = 2

# Ball
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_R*2, BALL_R*2)
ball_speed = [4, 4]

# Initialisation
score = 0
font = pygame.font.SysFont("Arial", 24)

# Police
obstacle_img = pygame.image.load("miscelanious/police.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (OBSTACLE_R*2, OBSTACLE_R*2))

# Floyd
help_img = pygame.image.load("miscelanious/floyd.png").convert_alpha()
help_img = pygame.transform.scale(help_img, (HELP_BALL_R*2, HELP_BALL_R*2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(10, 0)

    # --- Drop obstacle ---
    obstacle.y -= obstacle_speed[1]

    # --- Obstacle reset ---
    if obstacle.bottom >= HEIGHT:
        obstacle.top = 0
        obstacle.x = random.randrange(0, WIDTH - obstacle.width)

    # --- Obstacle hit ---
    if obstacle.colliderect(paddle):
        score = 0
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed = [4, -4]

    # --- Randomly spawn help ball ---
    if not help_active and random.randint(1, 140) == 1:
        help_ball.x = random.randrange(0, WIDTH - help_ball.width)
        help_ball.y = 0
        help_active = True

    # --- Move objects ---
    if help_active:
        help_ball.y += help_fall

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # --- Collisions ---
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    if help_active:
        if help_ball.colliderect(paddle):
            score += 1
            help_active = False
        if help_ball.top >= HEIGHT:
            help_active = False

    # --- Game over ---
    if ball.bottom >= HEIGHT:
        score = 0
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed = [4, -4]

    # --- Draw (after all updates) ---
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    screen.blit(obstacle_img, obstacle)
    if help_active:
        screen.blit(help_img, help_ball)
    text = font.render(f"Fentanyl: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
