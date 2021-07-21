"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/


NOTE: 
    - While we are traversing we can decide whether to add None nodes to queue
    - Option 1:  Only add value nodes to queue
        - pop queue. we know it is value node
        - check if child isnt None before appending
    - Option 2:  We can add None nodes to queue
        - Pop queue. It might be none, and we cant access child of none
        - IF not None, append left and right child (might be None)
"""
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        
        if not root:   
            return levels
        
        q = deque([root])
        
        # while q, iterate thru all elemements in q using for loop
        while q: 
            # elements of this tree level
            level = []
            level_size = len(q)
            
            # wrap the pop and appending in a for loop over level_size
            for _ in range(level_size):
                node = q.popleft()

                # Process node, do something with it
                level.append(node.val)
                
                if node.left:     
                    q.append(node.left)
                if node.right:    
                    q.append(node.right)
                    
            levels.append(level)
            
        return levels