
"""
Similar to merging two sorted arrays.
Make a dummy to initialize l3

Time: O(m + n)
Space: O(1)
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p3 = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                new_node = ListNode(p1.val)
                p3.next = new_node
                p3 = new_node
                p1 = p1.next
            else:
                new_node = ListNode(p2.val)
                p3.next = new_node
                p3 = new_node
                p2 = p2.next
        # exit loop, check any remain vals
        if not p1:
            p3.next = p2
        else:
            p3.next = p1
        
        return dummy.next