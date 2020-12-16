# https: // leetcode.com/problems/add-two-numbers/
"""
Intuition:
Iterate over both lists, from ones place first node onwards...
Add values of both lists. NOTE: And any leftover carry
    - Take last digit. Use that to initialize new node and append to result list
    - If sum > 10, carry = 1
NOTE: after we run out of digits. we can still have a carry. Add ONE MORE node of value 1

Time: O(a + b) or O( max(a,b) )
Space: O( max(a,b) + 1)
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p1 = l1
        p2 = l2
        p3 = dummy
        carry = 0

        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0

            # max 18
            xy_sum = x + y + carry
            last_digit = xy_sum % 10
            carry = 1 if xy_sum >= 10 else 0

            # new node with value of last digit
            new_node = ListNode(last_digit)
            p3.next = new_node
            p3 = p3.next

            # iterate list pointers if possible
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        # any leftover carry has to be added to new node
        if carry:
            new_node = ListNode(carry)
            p3.next = new_node
            p3 = p3.next
        return dummy.next
