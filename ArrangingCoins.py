class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        total = 0
        
        if n == 1:
            return 1
        
        while total < n:
            count = count + 1
            total = total + count
            print(total)
            
        return count - 1
            
n = 5

s = Solution()
print(s.arrangeCoins(n))