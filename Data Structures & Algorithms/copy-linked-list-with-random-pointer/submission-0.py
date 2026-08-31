import copy

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
        out = copy.deepcopy(head)
        return out
        # seen = {}
        # curr = head
        # while curr:
        #     if curr.next in seen:
        #         curr_next_value = seen[curr_next][0]
        #         curr.next = seen[]
        #     next_node = Node(curr.next.val, None, None)
        #     random_node = Node(curr.random.val, None, None)
