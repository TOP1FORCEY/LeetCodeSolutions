class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        
        if x[0] == "-":
            x = x[1:]
            x = int(x[::-1])
            if x < 2 ** 31:
                return x * -1
            return 0
        
        else:
            x = int(x[::-1])
            if x < 2 ** 31:
                return x
            return 0
            
num = -123

s = Solution()
print(s.reverse(num))