numRows = 5

class Solution(object):
    def generate(self, numRows):
        output = [[1]]
        if numRows == 0:
            return []
        for _ in range(numRows - 1):
            temp = [0] + output[-1] + [0]
            row = []
            for i in range(len(output[-1]) + 1):
                row.append(temp[i] + temp[i + 1])
            output.append(row)
        return output   
            

s = Solution()
print(s.generate(numRows))