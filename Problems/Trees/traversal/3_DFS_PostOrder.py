from collections import deque
"""
Recursive:
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        vals = []
        self.dfs(root,vals)
        return vals
    
    def dfs(self, root, vals):
        # implicit base case NONE node returns nothing

        # recursive case. call dfs on children
        if root:
            self.dfs(root.left, vals)
            self.dfs(root.right, vals)
            vals.append(root.val)
            
    
"""
Iterative: Deque for reversed results, Stack

Solve for Root -> Right -> Left ... instead
    - for stack we push left then right child
    - Append Values in reverse, by .appendleft() to deque
"""
class Solution3:
    def postorderTraversal(self, root):
        stack = [root]
        vals = []
        while stack:
            node = stack.pop()
            if node:
                vals.append(node.val)  #TODO: or we can append left to deque
                stack.append(node.left)
                stack.append(node.right)
        vals.reverse()
        return vals

