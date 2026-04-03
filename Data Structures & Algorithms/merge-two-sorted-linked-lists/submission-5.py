# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        #Edgcages if list 2 is none return list
        if not list1 and not list2:
            return None

        if not list2:
            return list1
        #vise versa
        if not list1:
            return list2

        #Create dummy node
        dummy = node = ListNode()

        #Create a while loop between listq and list2
        while list1 and list2:
            #check to see whcih is the smallest value
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        #just case if on eht link list is the smallest then we can put the remainder in there
        node.next = list1 or list2

        return dummy.next

        