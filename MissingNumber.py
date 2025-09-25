class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for a in range(len(nums) + 1):
            if a not in nums:
                return a
        
        
s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))