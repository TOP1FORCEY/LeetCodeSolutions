# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        for a in range(k):
            copy = head
            val = 0
            while copy.next:
                copy = copy.next
            else:
                val = copy.val    
            current = head
            while current.next.next:
                current = current.next
            current.next = None
            head = ListNode(val, head)
        
        return head
    
    def output(self, head):
        output = []
        while head:
            output.append(head.val)
            head = head.next
        return output
        
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
print(s.output(s.rotateRight(head, 2)))