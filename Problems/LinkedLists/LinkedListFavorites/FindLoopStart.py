
# https://leetcode.com/problems/linked-list-cycle-ii/
"""
Time: O(N) to find cycle, less than O(n) to go M steps
Space: O(1)

M = Distance to cycle entry (E)
K = Distance covered within cycle before meeting point (X)
L = length of cycle
n = number of cycles

Fast and slow meet at  M + K = 2(M + K) - nL
* We subtract integer multiples of cycle length to get fast to same spot in cycle as slow
Simplify to: M + K = nL

E --k--> X --M-->  E

Fast has progressed K distance into the loop from the entry point. If Fast covers M more distance,
then Fast has covered M + K, which is n WHOLE CIRCLES FROM ENTRY POINT.

Set slow to beginning. Set rate of Fast to same as slow.
We know slow AND fast are M distance from entry. When slow == fast, that is the entry node.
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # is there a cycle?
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            # increment before checking if fast == slow
            fast = fast.next.next
            slow = slow.next
            # fast meets slow at K steps front entry
            if fast == slow:
                break

        # If we broke while loop because we hit end of list
        if fast is None or fast.next is None:
            return None

        # found a cycle. Now we increment M steps
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
