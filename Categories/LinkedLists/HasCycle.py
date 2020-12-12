# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # empty list
        if not head:
            return False

        # if single item, slow would initially equal fast
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            # increment if fast isn't at end of list
            slow = slow.next
            fast = fast.next.next
        # broke out of loop. Slow is fast
        return True

