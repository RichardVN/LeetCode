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
"""
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []
        preorder_vals = []
        # recursively call dfs, starting at root, passing list we want to append
        # NOTE: we do not need to have dfs return anything, global list passed by reference
        self.dfs(root, preorder_vals)
        return preorder_vals
    
    # another method, with self parameter
    def dfs(self, root, res):
        # implicit base case NONE node returns nothing

        # recursive case. call dfs on children
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
"""
Iterative: Stack of tuples (Node, Visited?)

If visited, process node value
If not visited, add (node.leftright, False) and (Node, TRUE) to stack
"""
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        vals = []
        # stack contains tuples of (Node, Visited?)
        # Visited means we added children to stack already
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            # note: node or visited could be None ...
            if not node: continue
            # visited means we can process value
            if visited:
                vals.append(node.val)
            # not visited, means add children to stack & mark visited REVERSED
            # node -> L -> R  means push   R -> L -> node
            else:
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
        return vals
    
"""
Iterative Approach w/ Stack:
- Initialize stack with root, and result array
- stack initialized with root
- process Root first
- append children to stack in reverse order, if children is not NONE
"""
class Solution3:
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

