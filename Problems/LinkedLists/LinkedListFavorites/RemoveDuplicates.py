# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""
Intuition:
    - SORTED .. meaning dupes are adjacent.
    - 2 pointers: before, curr
    - if values of before and curr match, rewire before.next so that it skips over curr
    NOTE: before starts at None (similar to reverse list)
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        before = None

        while curr:
            # TODO: only rewire if before is actually at a node
            if before and before.val == curr.val:
                before.next = curr.next
            # node was not removed. before has to advance a node as well
            else:
                before = curr
            
            curr = curr.next
        return head