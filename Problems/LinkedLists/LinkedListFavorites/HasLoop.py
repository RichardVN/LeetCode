# https://leetcode.com/problems/linked-list-cycle/
"""
Intuiution: Fast and slow pointers until fast == slow
    Note that fast either ends on None OR fast.next ends on None, depending on list parity
    NOTE: Same as find middle of list, but with a break condition

Time complexity:
    - No Cycle: O(N) fast pointer reaches end
    - Cycle: O(N + K) where K is cyclic length, reduce O(N)
        - N steps for slow to enter cycle, and K iterations for fast to catch slow
        - NOTE: if fast behind slow:  Number loops to catch = distance between pointers / difference of speed
    - Space: O(1) , use constant space
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Do not enter loop if fast is on tail -- cannot step forward twice
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            # NOTE: if there is a cycle, we need a break condition
            if fast == slow:
                return True
        # fast reached a None --> No cycle
        return False

