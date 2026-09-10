# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        final_head = None
        previous_tail = None
        
        previous_tail = None
        while curr:
            # if k nodes are available
            temp = curr
            for i in range(k):
                if temp == None:
                    if previous_tail:
                        previous_tail.next = curr
                    if final_head:
                        return final_head
                    else:
                        return head
                temp = temp.next
            
            group_head, next_head, group_tail = self.reverse(curr, k)
            if final_head == None:
                final_head = group_head
            if previous_tail:
                previous_tail.next = group_head
            previous_tail = group_tail
            group_tail.next = next_head
            curr = next_head

        return final_head 
        
    def reverse(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        curr = head
        h = head
        for i in range(k):
            nex = curr.next
            curr.next = prev
            prev = curr 
            curr = nex
        if curr:
            h.next = curr
        return prev, curr, h  
