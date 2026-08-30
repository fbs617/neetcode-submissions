# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        prev = None
        while length != n:
            length -= 1
            prev = curr
            curr = curr.next
        next_node = curr.next
        if curr == head:
            head = head.next
        if prev:
            prev.next = next_node
        return head
        
        
        
        