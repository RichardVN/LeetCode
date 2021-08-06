# https://leetcode.com/problems/reverse-linked-list/
"""
Approach: triple pointer
Time: O(N) to transverse list
Space: O(1) only pointers

NOTE:  Initialize before to None, current to head. In loop: after = current.next, current
        -> Remember to return BEFORE, which will be new head

Intuition:
    1. Initialize three pointers. 
        Before = None
        Current = head
        After = head
    2. Step through list while current is not None:
        a. Set after to node after current
        b. redirect current.next
        c. step before to current
        d. step current to after
    3. NOTE: return before, tail of old list, and HEAD of reversed list
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
            # reverse the next "arrow"
            curr.next = before
            # move before up a node, move current up a node (DONT USE NEXT)
            before = curr
            curr = after

        return before
