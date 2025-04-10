array = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums = list):
    """
    :type nums: List[int]
    :rtype: int
    """
    initlen = len(nums)
    action = True
    i = 0

    while action:
        
        action = False
        
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            nums.pop(i + 1)
            action = True
        
        elif i + 1 < len(nums) and nums[i] <= nums[i + 1]:
            i += 1
            action = True
    
    

    return initlen - len(nums), nums



print(removeDuplicates(array))