# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        length_mid = 0
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
        if slow.next == None:
            return
        curr = slow.next
        slow.next = None
        prev = curr
        
        next_node = curr.next
        curr.next = None
        curr = next_node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_list = prev
        
        curr1 = head

        while second_list:
            next_node1 = curr1.next
            next_node2 = second_list.next
            curr1.next = second_list
            second_list.next = next_node1
            second_list = next_node2
            curr1 = next_node1


