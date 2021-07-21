"""
Approach 1:  BFS using queue 

Approach: BFS level by level to connect right pointers
    KEY NOTE: 
        - we can peek the queue for connections, without popping yet
        - make sure to check that i pointer is NOT on last node of the level
            before we try to connect to next node on queue
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.bfs(root)
        return root
    
    def bfs(self, root):
        q = deque([root])
        while(q):
            level_size = len(q)
            # NOTE: we can connect without popping
            for i in range(level_size):
                node = q.popleft()
                # add children to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # assign next ptr if NOT last node on level. Dont want to next -> next level
                if i != level_size - 1:
                    node.next = q[0]

"""
Approach 2:  Pointers only O(1) space

Intuition: 
    WHILE LEFTMOST
    - Leftmost ptr iterates level by level
    WHILE HEAD
    - head ptr iterates node to node, on leftmost's level
        - Connection 1: head.left.next = head.right 
        - Connection 2: head.right.next = head.next.left  (IF head.next)
        - Progress head = head.next

"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 