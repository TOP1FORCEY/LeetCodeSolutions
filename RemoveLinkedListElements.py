# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current = ListNode()
        dummy = current
        
        while head:
            print(head.val)
            if head.val != val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        
        return dummy.next
        
        
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(4)))))
val = 4
s = Solution()
print(s.removeElements(head, val))