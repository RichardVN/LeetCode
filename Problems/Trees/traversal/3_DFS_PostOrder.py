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
Iterative: Stack of tuples (Node, Visited?)

If visited, process node value
If not visited, add (node.leftright, False) and (Node, TRUE) to stack
"""
class Solution2(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        vals = []
        # stack contains tuples (node, visited?)
        stack =[(root, False)]

        while stack:
            node, visited = stack.pop()
            # check if node isnt NONE
            if node:
                # if visited, process value
                if visited:
                    vals.append(node.val)
                # if not visited, add children to stack, mark node as visited
                else:
                    # left -> right -> root REVERSED cuz stack
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return vals
    
"""
Iterative: Deque for reversed results, Stack

Solve for Root -> Right -> Left ... instead
    - for stack we push left then right child
    - Append Values in reverse, by .appendleft() to deque
"""
class Solution3:
    def postorderTraversal(self, root):
        print("iterative with deque")
        if not root: 
            return []
        res_vals = deque()
        stack = [root]

        while stack:
            node = stack.pop()
            # we add to results list from left side
            res_vals.appendleft(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res_vals

