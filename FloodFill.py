class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:   
        rows = len(image)
        cols = len(image[0])
        queue = [(sr,sc)]
        old_color = image[sr][sc]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if old_color == color:
            return image
                
        while len(queue) > 0:
            r, c = queue.pop(0)
            if image[r][c] == old_color:
                image[r][c] = color
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if image[nr][nc] == old_color:
                            queue.append((nr, nc))
            
        return image
            
            
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2

s = Solution()
print(s.floodFill(image, sr, sc, color))