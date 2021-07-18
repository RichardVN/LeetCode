"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
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