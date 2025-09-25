class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        a = 1
        
        while a <= n:
            
            if a % 3 == 0 and a % 5 == 0:
                output.append("FizzBuzz")
            elif a % 3 == 0:
                output.append("Fizz")
            elif a % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(a))
            
            a += 1
        
        return output
    
n = 15
s = Solution()
print(s.fizzBuzz(n))