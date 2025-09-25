class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        
        
class Solution(object):
    def removeNthFromEnd(self, nums = ListNode, val = int):
        
        write_index = 0
    
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
    
        return write_index
                