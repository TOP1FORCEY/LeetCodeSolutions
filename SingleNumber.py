class Solution(object):
    def singleNumber(self, nums = list):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        while len(nums) != 1:
            for pos1, initial in enumerate(nums):
                for pos2, search in enumerate(nums):
                    if initial == search and pos1 != pos2:
                        nums.remove(search)
                        nums.remove(initial) 

        return nums[0]
            

nums = [4,1,2,1,2]
s = Solution()
print(s.singleNumber(nums))