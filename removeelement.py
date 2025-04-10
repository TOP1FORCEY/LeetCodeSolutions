nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums = list, val = int):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        count = 0
        changed = True    
        
        while changed:
            changed = False
            ref = list()
            for a in nums:
                ref.append(a)

            for i in range(len(nums)):
                if nums[i] == val:
                    num = nums[i]
                    nums.pop(i)
                    nums.append(num)
                    break
            
            if nums != ref:
                changed = True
        
        for num in nums:
             if num != val:
                  count += 1
        
        return count, nums

print(removeElement(nums, val))