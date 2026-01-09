class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    # up
                    if y == 0 or grid[y - 1][x] == 0:
                        perimeter += 1
                    # down
                    if y == rows - 1 or grid[y + 1][x] == 0:
                        perimeter += 1
                    # left
                    if x == 0 or grid[y][x - 1] == 0:
                        perimeter += 1
                    # right
                    if x == cols - 1 or grid[y][x + 1] == 0:
                        perimeter += 1

        return perimeter
    
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

s = Solution()
print(s.islandPerimeter(grid))