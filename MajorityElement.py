class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}
        for element in nums:
            try:
                elements[element] += 1
            except:
                elements[element] = 1
        
        return max(elements, key = elements.get)
            
        
        
nums = [2,2,1,1,1,2,2,1,1]
s = Solution()
print(s.majorityElement(nums))
