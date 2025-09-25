class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
            
nums = [1,2,3,1]

s = Solution()
print(s.containsDuplicate(nums))