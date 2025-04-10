
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

num = ListNode(1, ListNode(1, ListNode(2, ListNode(3,ListNode(3, ListNode(4, None))))))

def deleteDuplicates(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        temp = head

        while temp and temp.next:            
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        output = [] # this part of the script is only specific to VScode for more apealing output in the terminal : )
        while head is not None:
            output.append(head.val)
            head = head.next

        return output

print(deleteDuplicates(num))