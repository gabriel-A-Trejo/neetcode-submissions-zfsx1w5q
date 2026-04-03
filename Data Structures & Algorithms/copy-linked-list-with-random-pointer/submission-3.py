"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Checke to head is not none
        if not head:
            return None

        new = {}

        curr = head

        while curr:
            if curr not in new:
                new[curr] = Node(curr.val)
            if curr.next:
                if curr.next not in new:
                    new[curr.next] = Node(curr.next.val)
                new[curr].next = new[curr.next]
            if curr.random:
                if curr.random not in new:
                    new[curr.random] = Node(curr.random.val)
                new[curr].random = new[curr.random]
            
            curr = curr.next
        return new[head]


