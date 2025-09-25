class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        if n % 2 == 1:
            result.append(0)
        
        return result
    
n = 10
s = Solution()
print(s.sumZero(n))
print(sum(s.sumZero(n)))