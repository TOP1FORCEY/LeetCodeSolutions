class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) * int(num ** 0.5) == num
        
num = 26

s = Solution()
print(s.isPerfectSquare(num))