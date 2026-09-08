class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                second = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(lists[i], second))
            lists = merged
        return lists[0]

    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
        else:
            head = list2
            list1, list2 = list2, list1

        prev = None
        while list1 and list2:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                nex = list2.next
                list2.next = prev.next
                prev.next = list2
                prev = list2
                list2 = nex
        if list2:
            prev.next = list2
        return head