class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        while len(num) != 1:
            numbers = []
            for symbol in num:
                numbers.append(int(symbol))
            num = str(sum(numbers))
        
        return int(num)


num = 89

s = Solution()
print(s.addDigits(num))