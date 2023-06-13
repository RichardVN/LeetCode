
#  https://leetcode.com/problems/reorder-list/editorial/
"""
1. Find Mid and Mid -1
2. Reverse second half
3. Merge both lists into third list

Time: O(N)
Space: O(1), no additional data structures
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point, and node before mid
        f = s = head
        t = None
        while f and f.next:
            f = f.next.next
            t = s   # mark t before step  s
            s = s.next
        mid = s
        t.next = None

        # Slow is at middle (odd) or SECOND middle (even)
        # iff odd list, L2 will have one more node than l1

        # reverse list
        curr = mid
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        l2 = prev

        # now we have the 2 lists
        l1 = head

        # dummy for result list
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            print(f"{l1.val=} {l2.val=}")
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next
        # note l2 can have one more node
        if l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        return dummy.next