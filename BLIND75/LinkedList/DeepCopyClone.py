# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
Problem from random pointer:
    - No way to go backwards from given node
    - random could point forwards to a node that hasn't been created yet
    - You have to ensure that if two nodes point to the first node, you don't create a duplicate
NOTE: 
    Node1  --> Node2
      |          |
    Clone1    Clone2

- Each original node in the linked list is mapped with a clone node. There are no duplicate nodes of same address.
- We can access in O(1) time the current's clone, or the .next's clone, or the .random's clone
- ** Given a ptr to a Node, we can access any nodes it points to in O(1) time.
    - If ALL nodes are in a hash map as keys, we can then access the key-value pairs in O(1) time.

Intuition:
1. Create a hash map
2. Traverse original nodes.
    a. Place original nodes as hash keys
    b. Place new Node Clones as hash values
3. Second pass of original nodes.
    a. Connect clone's next, random ptrs to
    the clones of original's next, random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # for any node, map the node to its clone
        node_to_clone = dict()
        # TODO:  if random points to none instead of node
        node_to_clone[None] = None
        # create clone nodes mapped to original nodes, unlinked
        current = head
        while current:
            # instantiate clone. NOTE: make new node, dont
            # use current ptr, which points to same original node
            # key : value,   Node ptr: clone node
            cloned_node = Node(current.val)
            node_to_clone[current] = cloned_node
            current = current.next

        # link clone nodes
        current = head
        clone_head = node_to_clone[head]
        while current:
            clone = node_to_clone[current]
            # clone's next is the CLONE of current.next
            clone.next = node_to_clone[current.next]
            # clone's random is the CLONE of current.random
            clone.random = node_to_clone[current.random]
            current = current.next

        return clone_head
