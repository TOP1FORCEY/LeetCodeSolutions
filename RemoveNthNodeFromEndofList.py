# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head = ListNode, n = int):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        skip = self.getHeadCount(head) - n
        count = 0
        
        if skip == 0:
            return head.next
        
        current = ListNode()
        dummy = current
        
        while head:
            if count != skip:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
            count += 1

            
        return dummy.next
                
    def getHeadCount(self, head):
        count = 0
        if head:
            while head.next is not None:
                count += 1
                head = head.next
            count += 1
        return count
           
           
            

def output(list):
    output = []
    if list:
        while list.next is not None:
            output.append(list.val)
            list = list.next
        output.append(list.val)
    return output


head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
n = 2

s = Solution()
print(output(s.removeNthFromEnd(head, n)))