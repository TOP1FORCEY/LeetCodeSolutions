class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        matrix = []
        for y in range(m):
            row = []
            for x in range(n):
                row.append(0)
            matrix.append(row)
            
        if ops is not None:
            for op in ops:
                for y in range(op[0]):
                    for x in range(op[1]):
                        matrix[y][x] += 1
        
        nums = []
        for row in matrix:
            for n in row:
                nums.append(n)

        return nums.count(max(nums))
        
            
    
m = 39999
n = 39999
ops = [[19999,19999]]

s = Solution()
print(s.maxCount(m,n,ops))