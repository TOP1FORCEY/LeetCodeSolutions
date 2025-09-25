class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        outputs = []
        
        while n != "1":
            output = 0
            for symbol in n:
                output += int(symbol) ** 2 
                n = str(output)
            if output in outputs:
                return False
            else:
                outputs.append(output)
                
        return True
        
        
n = 20
s = Solution()
print(s.isHappy(n))