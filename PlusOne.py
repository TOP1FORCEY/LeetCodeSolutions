digits = [4,3,2,1]

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ""

        for num in digits:
                number = number + str(num)
        
        output = int(number) + 1

        return [int(i) for i in str(output)]

print(plusOne(digits))