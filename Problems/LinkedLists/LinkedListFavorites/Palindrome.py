# https://leetcode.com/problems/palindrome-linked-list/description/
"""
Solution 1 
Intuition: Convert list array. Walk ptrs in from the ends to mid, ensuring vals are equal

Advantage: Don't mess with original list value
Time: O(N) copy to list
Space: O(N) list
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        # transform to list
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        l = 0
        r = len(lst) - 1

        # walk pointers in from ends
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        
        return True


"""
Solution 2 - OPTIMAL TIME, but modify input
Intuition: 
    1. Find midpoint of linked list using fast, slow pointers. It does not matter if we find the left or right mid in even list.
    2. Reverse the second half of linked list from mid onwards.
    3. Iterate through both partitions, return true if made it to end of one partition w/o unequal values.

Advantage: Constant space
Time: O(N) find midpoint O(N) reverse O(N) iterate through both halves
Space: O(1) just pointers
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # empty list is a palindrome
        if not head:
            return True

        # find mid node
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is now the mid node

        # reverse from mid node to end of list
        slow = self.reverse_list(slow)

        # loop through both halves to check if vals are the same
        fast = head
        # go through left half and reverse right half. One list might be one node longer
        while fast and slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        # reach end of one of lists
        return True

    def reverse_list(self, head):
        before = None
        current = head
        after = head

        while current:
            # save the spot of next node before moving next ptr
            after = current.next
            current.next = before
            before = current
            current = after
        # new head is at before
        return before
