# https://leetcode.com/problems/remove-linked-list-elements/
"""
Time: O(n)
Space: O(1)

NOTE: we need the node before the node w/ bad value to reassign
        since we access current.next.val, we have to ensure current.next is not None
        Reassign head to the node next to dummy value
"""

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        # dummy in front of original head
        dummy = ListNode(-1)
        dummy.next = head

        current = dummy
        while current.next is not None:
            # Do not step current yet. The new next could also contain bad value
            # Are we safe to access current.next.next. YES we confirm that current.next is NOT None
            if current.next.val == val:
                current.next = current.next.next
            # the next's val is good. We can step to it
            else:
                current = current.next
        # reassign head
        head = dummy.next

        return head
