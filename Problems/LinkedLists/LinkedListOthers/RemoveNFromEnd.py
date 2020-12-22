# https: // leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
Time: O(N) to get size, O(N) to remove element
Space: O(1)

NOTE: you can two ptrs, that are n nodes apart. Advance both while maintaining n gap.
        Remove the node at slow upon reaching end. This is one pass.

To have current end on a i - 1 node
    for i in range(i-1):
        current = current.next
"""
# GIVEN:
# list is n elements, in range [1, 30]
# values can only be [0, 100]
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # First Pass: get size
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        # Second Pass: remove at index
        # remove head:
        if size == n:
            head = head.next
        # remove another node:
        else:
            idx_remove = size - n
            # find node before removal
            current = head
            for i in range(idx_remove - 1):
                current = current.next
            # current now at before node. Skip the node to remove
            current.next = current.next.next

        return head
