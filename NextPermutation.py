class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # cheking if permutation is possible
        count = 1
        
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
        if count == len(nums):
            nums[:] = nums[::-1]
            return nums
        else:
            pivot = -1
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    pivot = i
                    break
            swap = []
            for i in range(pivot + 1, len(nums)):
                swap.append(nums[i])
            
            candidates = []
            for i in range(pivot + 1, len(nums)):
                if nums[i] > nums[pivot]:
                    candidates.append(nums[i])

            if candidates:
                target_value = min(candidates)
                nindex = nums[pivot + 1:].index(target_value) + pivot + 1
                nums[pivot], nums[nindex] = nums[nindex], nums[pivot]
            
            nums[pivot + 1:] = sorted(nums[pivot + 1:])
                
            return nums



#nums = [3, 2, 1]
nums = [1, 3, 2]
s = Solution()
print(s.nextPermutation(nums))