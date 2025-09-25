class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        output = 0

        for i in range(0, len(nums), 2):
            output += nums[i]
            
        return output


nums = [1,4,3,2]
s = Solution()
print(s.arrayPairSum(nums))