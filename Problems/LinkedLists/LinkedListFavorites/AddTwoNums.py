# https://leetcode.com/problems/add-two-numbers/
"""
CATCHES:
- must consider carry into digit total. And calculate new carry
- check that the ptr is not at None, before accessing .val and iterating ptr
- after while loop, check for carry and add additional node if necessary

Pseudo:
Iterate over both lists, from ones place first node , then tens place .. etc
Add values of both lists. NOTE: And any leftover carry
    - Take last digit. Use that to initialize new node and append to result list
    - If sum > 10, carry = 1
NOTE: after we run out of digits. we can still have a carry. Add ONE MORE node with value 1

Time: O(a + b) or O( max(a,b) )
Space: O( max(a,b) + 1)
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # new list
        dummy = ListNode(-1)

        i = l1
        j = l2
        k = dummy

        # carry
        carry = 0

        while i or j:
            # 1. add values and ANY leftover carry
            val1 = i.val if i else 0
            val2 = j.val if j else 0
            total = val1 + val2 + carry

            # 2. Calculate new carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0
            
            # 3. Create new Node for total
            new = ListNode(total)
            k.next = new
            k = new

            # iterate pointers if possible
            if i:
                i = i.next
            if j:
                j = j.next
        # TODO: 4. if we still have carry, we still need to make node
        if carry:
            # create new node. Connect. Step.
            new = ListNode(carry)
            k.next = new
            k = new
        return dummy.next
