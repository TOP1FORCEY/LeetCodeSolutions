class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = []
        output = [num]
        
        for a in str(num):
            nums.append(int(a))
        
        for pos, num in enumerate(nums):
            
            cnums = nums[:]
            
            if num == 9:
                cnums.pop(pos)
                cnums.insert(pos, 6)
            else:
                cnums.pop(pos)
                cnums.insert(pos, 9)
            
            output.append(int("".join(str(d) for d in cnums)))
               
        return max(output)

num = 9999

s = Solution()
print(s.maximum69Number(num))