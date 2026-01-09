class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        output = []
        
        for n in set1:
            if n in set2:
                output.append(n)
        
        return output
        
nums1 = [1,2,2,1]
nums2 = [2,2]

s = Solution()
print(s.intersection(nums1, nums2))