"""
Recursive
"""
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vals = []
        self.dfs(root, vals)
        return vals
        
    # in order:  left -> root -> right
    def dfs(self, root, vals):
        # implicit base case NONE node returns nothing

        # recursive case. call dfs on children
        if root:
            self.dfs(root.left, vals)
            vals.append(root.val)
            self.dfs(root.right, vals)

"""
Iterative: Stack of tuples (Node, Visited?)

If visited, process node value
If not visited, add (node.leftright, False) and (Node, TRUE) to stack
"""
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        # let stack contain tuple of (node, visited?)
        # Visited TRUE meaans that we have already appended its children
            # and that node is ready for processing
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node:
                # ready for process
                if visited:
                    vals.append(node.val)
                # we push to stack in reverse order ... right -> root -> left
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return vals
            