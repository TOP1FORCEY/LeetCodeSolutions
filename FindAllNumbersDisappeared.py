class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(list(range(1, len(nums) + 1))) - set(nums))
        
        
nums = [4,3,2,7,8,2,3,1]

s = Solution()
print(s.findDisappearedNumbers(nums))