# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        i = head
        j = head.next
        while i != j and j != None and j.next != None:
            i = i.next
            j = j.next.next
        if i == j:
            return True
        else:
            return False