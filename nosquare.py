x = 8

def mySqrt(x = int):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        
        while i * i <= x:
            i += 1

        return i - 1



print(mySqrt(x))