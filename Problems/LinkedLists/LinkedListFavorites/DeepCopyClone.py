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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = head

        # we need to have copy equivalent of NONE "node"
        oldToCopy = {None:None}

        # build out the nodes
        while c:
            newNode = Node(c.val)
            oldToCopy[c] = newNode
            c = c.next
        
        c = head

        # wire the nodes
        while c:
            # access copy node
            copyNode = oldToCopy[c]
            # add wiring ... wire to COPIES as well
            copyNode.next = oldToCopy[c.next] 
            copyNode.random = oldToCopy[c.random]
            c = c.next

        return oldToCopy[head]
