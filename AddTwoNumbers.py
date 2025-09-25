# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = ""
        num2 = ""
        
        while l1.next:
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
        
        while l2.next:
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        
        sum = list(str(int(num1[::-1]) + int(num2[::-1]))[::-1])
        output = head = ListNode(int(sum[0]))
                
        for num in sum[1:]:
            head.next = ListNode(int(num))
            head = head.next
            
        return output
            
l1 = ListNode(2,ListNode(4, ListNode(3)))        
l2 = ListNode(5,ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(l1, l2))