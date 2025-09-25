class Solution(object):
    def findLHS(self, nums = list):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)  
        l = len(nums)
        i = 0
        j = 0
        best = 0
        print(nums)
        
        while j < l:
            print(best, nums[j], nums[i])
            if nums[j] - nums[i] > 1:
                i += 1
            else:
                if nums[j] - nums[i] == 1:
                    best = max(best, j - i + 1)
                j += 1
        return best
        
        
nums = [1,3,2,2,5,2,3,7]

s = Solution()
print(s.findLHS(nums))