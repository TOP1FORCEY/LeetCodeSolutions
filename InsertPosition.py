nums = [1,3,5,6]
target = 4

def searchInsert(nums = list, target = int):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        if target < nums[0]:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] < target and target < nums[i + 1]:
                return i + 1
        return len(nums)




print(searchInsert(nums, target))