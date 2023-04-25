"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
Intuition:
    - Fast and slow pointer until fast hits end
    - return slow
    NOTE: Same as has cycle, but without the break

EVEN (slow ends at 2nd middle)
                      f
            s
  1 -> 2 -> 3 -> 4 -> NONE

ODD
            f
       s
  1 -> 2 -> 3 -> NONE

Time: O(N) for fast to reach end
Space: O(1) since we use pointers

"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow