# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0  # indicates whether or not we carry over the one
        curr1 = l1
        curr2 = l2
        new_head = ListNode(0, None)
        new_head_val = curr1.val + curr2.val
        if new_head_val >= 10:
            new_head_val %= 10
            carry_over = 1
        new_head.val = new_head_val
        curr = new_head
        curr1 = curr1.next
        curr2 = curr2.next
        while curr1 or curr2:
            curr_next_val = 0
            if curr1 == None:
                curr_next_val = curr2.val + carry_over
            elif curr2 == None:
                curr_next_val = curr1.val + carry_over
            else:
                curr_next_val = curr1.val + curr2.val + carry_over
            carry_over = 0
            if curr_next_val >= 10:
                curr_next_val %= 10
                carry_over = 1
            curr.next = ListNode(curr_next_val, None)
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            curr = curr.next
        if carry_over == 1:
            curr.next = ListNode(1, None)
        return new_head
