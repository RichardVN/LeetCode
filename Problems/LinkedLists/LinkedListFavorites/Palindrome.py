
"""
Solution 1 
Intuition: Convert list into deque so we can pop from both ends in constant time. Make sure pops.vals are equal

Advantage: Don't mess with original list value
Time: O(N) copy to deque and pop from deque
Space: O(N) deque
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # append nodes to deque
        d = deque()
        current = head
        # O(N)
        while current:
            d.append(current)
            current = current.next
        # O(N)
        while len(d) > 1:
            left_node = d.popleft()
            right_node = d.pop()
            if left_node.val != right_node.val:
                return False
        return True


"""
Solution 2 - OPTIMAL
Problem: We cannot iterate backwards from end like an array (no 'prev')
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
