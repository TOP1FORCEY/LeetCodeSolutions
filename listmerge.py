list1 = [1,2,4]
list2 = [1,3,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head

        while list1 and list2:

                print(current.next)

                if list1.val < list2.val:
                        current.next = list1
                        list1 = list1.next
                else:
                        current.next = list2
                        list2 = list2.next
                current = current.next
                
        current.next = list1 or list2

        print(head)

        return head.next