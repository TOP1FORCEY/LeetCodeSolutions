# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        split = 0
        splt = False
        
        count = head
        
        while count:
            split += 1
            count = count.next
        
        if split == 1:
            return True
        
        if split % 2 != 0:
            split -= 1      
            splt = True
        
        
        l1 = []
        
        for _ in range(int(split / 2)):
            l1.append(head.val)
            head = head.next
        
        if splt:
            head = head.next
        
        l2 = []
        
        for _ in range(int(split / 2)):
            l2.append(head.val)
            head = head.next
        
        return l1, l2, l1 == l2[::-1]
    
    
head = ListNode(1,ListNode(0,ListNode(1)))        

s = Solution()
print(s.isPalindrome(head))