"""
Binary search tree:
Q:  what is guaranteed?
    - at any node, nodes to right will have higher value. Nodes to left will have lower value
    - p and q are unique, if we reach a node that is either p/q, it has to be LCA
    
Intuition:  Start Current at root. Move current until p and q split
    - Start at ROOT: root is ancestor of all nodes
    - if both p and q are less than or greater than current.val, we can find a lower LCA
    - NOTE: if p and q are other sides of current.val, then they split into different trees
        - the root where split occurs is LCA
    - NOTE: if current.val is equal to p or q, then it HAS to be LCA
    
TIME: O(N) worst case skewed tree
Space: O(1)

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        # p and q are given NODES
        p_val = p.val 
        q_val = q.val
        while current:
            # TODO: careful with AND
            if p_val > current.val and q_val > current.val:
                current = current.right
            elif p_val < current.val and q_val < current.val:
                current = current.left 
            else:   # p and q are split OR p / q equal to current.val 
                return current
        return None