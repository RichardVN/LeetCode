
# https://leetcode.com/problems/linked-list-cycle-ii/
"""
Intuition:
    - 1. Use Floyd's cycle detection
    NOTE: While loop can break if 1. Fast reaches end (no cycle) OR 2. cycle is found
    - 2. Move Slow to beginning. Walk both pointers one node at a time

h = distance from head to cycle entry (E)
d = distance from cycle entry (E) to intersection point (X) 
L = length of cycle loop
                  _____
                 /     \
head -----h---- E       \(d)
             (t)\       /
                 X_____/

NOTE:
Slow has travelled h distance to loop, and d distance inside loop   ->   h + d 
Fast has travelled twice the distance as slow, with nL nodes extra  ->   h + d + t + d  + nL  ... Disregard nL since it leads to same spot

2 * Slow = Fast
Fast and slow meet at  2(h + d)  = h + d + t + d 
                        h + d = t + d
                        h = t

Distance beginning to X is same as X to loop entry
    - move slow to beginning and walk pointers one node at a time to find the intersection


Set slow to beginning. Set rate of Fast to same as slow.
We know slow AND fast are h distance from entry. When slow == fast, that is the entry node.

Time: O(N) to find cycle, less than O(n) to go h steps
Space: O(1)
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
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

        # TODO: If we broke while loop because we hit end of list
        if fast is None or fast.next is None:
            return None

        # found a cycle. Now we increment M steps
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
