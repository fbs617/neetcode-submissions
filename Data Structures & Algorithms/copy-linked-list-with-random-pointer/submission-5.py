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
        if head == None:
            return
        created = {}
        curr = head
        prev = None
        while curr:
            new_node = Node(curr.val, None, None)
            if prev:
                prev.next = new_node
            prev = new_node
            if len(created) == 0:
                new_head = new_node
            created[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            if curr.random in created:
                created[curr].random = created[curr.random]
            curr = curr.next
        return new_head
