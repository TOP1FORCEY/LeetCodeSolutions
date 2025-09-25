class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1


n = 60
s = Solution()
print(s.isPowerOfThree(n))