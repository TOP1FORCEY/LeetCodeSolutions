class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        nums = list(nums)
        
        if len(nums) < 3:
            return max(nums)
        
        for _ in range(2):   
            i = max(nums)
            nums = [x for x in nums if x != i]
            
        return max(nums)        
        
nums = [1, 1, 2, 2, 3, 4]
s = Solution()
print(s.thirdMax(nums))