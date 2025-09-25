class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        for power in range(1, 33):
            if n == 2 ** power:
                return True
        return False
        
        

n = 123
s = Solution()
print(s.isPowerOfTwo(n))