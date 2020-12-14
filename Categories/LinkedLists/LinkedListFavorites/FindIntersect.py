"""
Time: O(a+b) if we transverse both lists entirely
Space: O(1)

example diagram:

        a1 -> a1 ->
                    c1 -> c2 -> NONE
b1 -> b2 -> b2 ->

Let A nodes before intersection be A
Let B nodes before intersection be B
Let C nodes after intersection be C

pointer A hits intersection after   A + C + B    nodes
pointer B hits intersection after   B + C + A    nodes

If we increment one node at a time, they will eventually hit an intersection, IF they can jump lists
If there is NO intersection. Then they will meet at NONE "node" after a + b steps (transverse both lists)
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # Loop until pointers at same Node
        # guaranteed to meet at None, after a + b node iterations
        while pA is not pB:
            # NOTE: Ptr has to go ON None node BEFORE switch
            # so that ptrs can meet at None intersection if no other intersections
            # if at tail, switch lists
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            # if at tail, switch lists
            if pB is None:
                pB = headA
            else:
                pB = pB.next
        # loop breaks and pA = pB. (1) Pointers meet before None (2) Ptrs meet at None after both lists
        return pA
