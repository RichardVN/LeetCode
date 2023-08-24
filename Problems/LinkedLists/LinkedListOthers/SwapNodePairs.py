"""
Recursive Solution:
- Instead of While Loop, use recursion
- Recursive relation:  " List of swapped nodes = List of First 2 swapped + List of sub-remainder swapped "
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # takes in head of list to swap
        # returns new head of swapped list
        def dfsSwapped(head):
            # base
            if head is None or head.next is None:
                return head
            # recursive: "swapped list = swapped 2 nodes + swapped remainder of list"
            node1 = head
            node2 = head.next
            after = node2.next

            node2.next = node1
            node1.next = dfsSwapped(after)

            return node2 #TODO: node 2 is now the head of swapped list
        
        return dfsSwapped(head)


"""
Iterative solution:
- Dummy node to track new head
- While Loop
    - rewire first_node, second_node, and prev
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1) #TODO: using dummy node helps us to point to the new head
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next