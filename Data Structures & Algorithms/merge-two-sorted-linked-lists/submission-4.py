# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a dummy node  and has node = listNode 
        dummy = node = ListNode()
       
        #NExt step create a while loop for List1 and list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                  node.next = list2
                  list2 = list2.next
            node = node.next
        #check to see which is bigger list 1 or list 2 and upde node.next to new list
        #increment list 2 again
        node.next = list1 or list2



        #At the end of the while check to see any remainder 
        return dummy.next

        #return dummy .next
        