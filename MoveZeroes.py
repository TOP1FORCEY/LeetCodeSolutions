class Solution(object):
    def moveZeroes(self, nums = list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        
        for a in range(i, len(nums)):
            nums[a] = 0
        
        
        

nums = [0,1,0,3,12]
s = Solution()
print(s.moveZeroes(nums))