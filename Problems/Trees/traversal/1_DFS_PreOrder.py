"""
Preorder Traversal:  
    - read in value if we trace left side
    - Read ROOT -> LEFT -> RIGHT
    
Recursive Approach:
    - MAIN:
        - check not empty
        - Call DFS on main root
        - Return result array
    - DFS HELPER   NOTE: append, and call dfs in same order as traversal ROOT -> LEFT -> RIGHT
        - IF root:
            - append the root
            - call DFS on left, then right
        - ** Implied else is base case, eventually at end the root will be NONE
        
Iterative Approach:
- Initialize stack with root, and result array
- POP the stack to process it, add to result array
- PUSH / APPEND the child nodes to stack IF they exist
    - do in reverse order because we pop in reverse

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive solution, good if input small enough for call stack

class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []
        preorder_vals = []
        # recursively call dfs, starting at root, passing list we want to append
        # NOTE: we do not need to have dfs return anything, list passed by reference
        self.dfs(root, preorder_vals)
        return preorder_vals
    
    # another method, with self parameter
    def dfs(self, root, res):
        # check if root. Append to array in order  ROOT -> LEFT  -> RIGHT
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        # initialize stack with root
        stack = [root]
        vals = []
        
        while stack:
            # pop root to process first
            node = stack.pop()
            vals.append(node.val)
            # append root. Add children  right -> left, because stack is opposite
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return vals

