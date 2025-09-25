# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head = ListNode()):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        
        copy = head
        data = [head.val]
        while copy.next:
            copy = copy.next
            data.append(copy.val)
        data = data[::-1]
        
        head = None
        
        for i in data:
            node = ListNode(i)
            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node

        return head
        
        
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

s = Solution()
print(s.reverseList(head))