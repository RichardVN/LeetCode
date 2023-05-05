"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

TODO: 
    - We loop while queue
    - Within while loop, we have FOR loop over level size == len(q)


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
        
        # while q, iterate thru all elements in q using for loop
        while q: 
            # elements of this tree level
            level = []
            # level size is length of q, the nodes added by previous level
            level_size = len(q)
            
            # TODO: we are mutating queue. Thus we must use the level_size we recorded before.
            for _ in range(level_size):
                # pop front / left of queue
                node = q.popleft()
                # Process node value, write to level []
                level.append(node.val)
                
                # append children to back / right of queue
                if node.left:     
                    q.append(node.left)
                if node.right:    
                    q.append(node.right)
                    
            levels.append(level)
            
        return levels