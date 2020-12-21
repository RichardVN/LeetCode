# https://leetcode.com/problems/linked-list-cycle/
"""
Intuiution: Use Floyd's tortoise and hare to find cycle. 
    Note that fast either ends on None OR fast.next ends on None, depending on list parity

Time complexity:
    - No Cycle: O(N) fast pointer reaches end
    - Cycle: O(N + K) where K is cyclic length, reduce O(N)
        - N steps for slow to enter cycle, and K iterations for fast to catch slow
        - NOTE: if fast behind slow:  Number loops to catch = distance between pointers / difference of speed
    - Space: O(1) , use constant space
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Empty list
        if not head:
            return False
        fast = head
        slow = head
        # Iterate until fast is on tail node or the None after tail
        while fast is not None and fast.next is not None:
            # slow initially set same as fast. Make sure to increment first
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

