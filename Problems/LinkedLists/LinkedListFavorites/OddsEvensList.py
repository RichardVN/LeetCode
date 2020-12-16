# https://leetcode.com/problems/odd-even-linked-list/
"""
Time: O(N)
Space: O(1)
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd_head = odd_tail = head
        even_head = even_tail = head.next

        # both lists should end at None
        # NOTE: second condition necessary, because we essentially access even.next.next (move 2 nodes)
        # Loop breaks depending on how many nodes. Either breaks while even_tail is None, or even_tail.next is none
        while even_tail is not None and even_tail.next is not None:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next

            # this is accessing even_tail.next.next, therefore even_tail.next cant be none
            even_tail.next = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head

        return odd_head
