class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        preout = []
        
        for pos, num in enumerate(nums):
            if num == key:
                preout.append(pos)
        
        
        output = []
        n = len(nums)
        
        for pos in preout:
            L = max(0, pos - k)
            R = min(n - 1, pos + k)
            for a in range(L, R + 1):
                output.append(a)

        return sorted(set(output))
        
nums = [3,4,9,1,3,9,5]
key = 9
k = 1

s = Solution()
print(s.findKDistantIndices(nums, key, k))