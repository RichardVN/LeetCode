
"""
Similar to merging two sorted arrays.
Make a dummy to initialize l3

Time: O(m + n)
Space: O(1)
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # no need for special case empty or 1 node lists, handled by post-loop
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # in both cases, increment dummy pointer
            current = current.next
        # ran out of list for l1 or l2. Append the rest of remaining list including None
        if not l2:
            current.next = l1
        else:
            current.next = l2
        return dummy.next
