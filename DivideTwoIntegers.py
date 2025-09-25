class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        output = 0
        initdivisor = divisor
        ReturnNegative = False
        
        if abs(dividend) == abs(divisor):
            if dividend < 0 and divisor > 0:
                return -1
            elif dividend > 0 and divisor < 0:
                return -1
            else:
                return 1
        
        elif divisor == 1 and dividend > 0:
            output = dividend
            if output > 2147483647:
                return 2147483647
        elif divisor == 1 and dividend < 0:
            output = dividend
            if output < -2147483648:
                return -2147483648
        elif divisor == -1 and dividend < 0:
            output = dividend
            if output > 2147483647:
                return 2147483647
        elif divisor == -1 and dividend > 0:
            output = dividend
            if output > 2147483647:
                return 2147483647
            
        elif dividend < 0:
            ReturnNegative = True
            divisor = divisor * -1
            while dividend < divisor:
                output += 1
                divisor -= initdivisor
        
        elif divisor < 0:
            ReturnNegative = True
            dividend = dividend * -1
            while dividend < divisor:
                output += 1
                divisor += initdivisor
        else:
            while dividend > divisor:
                output += 1
                divisor += initdivisor
                
        if abs(output) >= 2147483648 and ReturnNegative == True:
            return max(int) * -1
        elif abs(output) >= 2147483648 and ReturnNegative == False:
            return max(int)
        
        if ReturnNegative == True:
            return output * -1
        return output
        
s = Solution()
print(s.divide(-7, 3))