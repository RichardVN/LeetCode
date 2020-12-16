# https://leetcode.com/problems/rotate-list/
"""
1. Find n, length of our list, by traversing. This is so we can get the "indices" of our nodes.
2. k = k % N.   If k is equal to N, we do a full lap (no shift). K < N for proper indexing.
3. We cut our list. The second part starts at N-Kth node. However, we need to go to the node before that to set it to point to None as new tail.
4. Find the tail of the original second part.
4. Connect the secont part's tail to the original head

TIME: O(N)
SPACE: O(1)
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # special cases, no rearrangment possible
        if head is None or head.next is None:
            return head

        # 1. get size of list
        N = 0
        current = head
        while current:
            N += 1
            current = current.next
        # 2. update k. Every N shifts is a full rotation (no change)
        k = k % N
        if k == 0:
            return head
        # 3. find Node before N - Kth index
        new_tail = head
        for _ in range(N - k - 1):
            new_tail = new_tail.next
        # new tail ends at node before -kth
        new_head = new_tail.next
        new_tail.next = None

        # find tail of new_head section so we can swap
        current = new_head
        while current.next:
            current = current.next
        current.next = head

        return new_head


"""
Solution 2:

Time: O(N)
Space: O(N)

Intuition: 
Convert linked list into array. 
Mod k into < size N. 
Shift left using negative indices
Populate new list using shifted array
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print('arr', arr)
        shifted_arr = [0] * len(arr)
        # k should be <= N
        k = k % len(arr)
        # shift right k, is shift left size - k
        for i in range(len(arr)):
            shifted_arr[i - (len(arr) - k)] = arr[i]

        dummy = ListNode(-1)
        cur = dummy
        for num in shifted_arr:
            new_node = ListNode(num)
            cur.next = new_node
            cur = cur.next
        return dummy.next
