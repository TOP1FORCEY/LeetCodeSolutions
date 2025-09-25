class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        for f in [2, 3, 5]:
            while n % f == 0:
                n = n // f
        return n == 1
       
s = Solution()
n = 7
print(s.isUgly(n))