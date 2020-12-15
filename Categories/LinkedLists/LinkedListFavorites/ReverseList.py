# https://leetcode.com/problems/reverse-linked-list/
"""
Time: O(N) to transverse list
Space: O(1) only pointers

NOTE: Triple pointer method. Before, current, after. Set after to current.next as FIRST step in while loop
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if empty, curr is None. Returns before is None
        # before is always the node before current
        before = None
        curr = head

        while curr:
            # on last iteration, after will be None
            after = curr.next
            curr.next = before
            before = curr
            curr = after

        return before
