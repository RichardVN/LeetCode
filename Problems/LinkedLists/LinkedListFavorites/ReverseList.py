# https://leetcode.com/problems/reverse-linked-list/
"""
Time: O(N) to traverse list
Space: O(1) only pointers

NOTE: Triple pointer method. Before, current, after. 
    - Set after to current.next as FIRST step in while loop

Intuition:
    1. Initialize three pointers. 
        Before = None
        Current = head
        After = head
    2. Step through list while current is not None:
        a. Set after to node after current
        b. redirect current.next
        c. step before to current
        d. step current to after
    3. NOTE: return before, tail of old list, and HEAD of reversed list
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if empty, curr is None. Returns before is None
        # before is always the node before current
        before = None
        curr = head

        while curr:
            # TODO: set after within loop
            after = curr.next
            # reverse the next "arrow"
            curr.next = before
            # move before up a node, move current up a node (DONT USE NEXT)
            before = curr
            curr = after
        # curr ends on NONE so return before
        return before


"""
Recursive solution:

- reverse everything besides head. 
- Set tail.next to head.  
- set head.next to NONE (b.c head is now the tail)

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            if head is None or head.next is None:
                return head
            
            after = head.next
            revList = rev(after)    # return head of reversed list
            after.next = head       # attach head to new tail end
            head.next = None        # head is now the tail

            return revList
        
        return rev(head)