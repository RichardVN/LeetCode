"""
KEY: when adding vals to result list, add to beginning of deque
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        vals = []
        self.dfs(root,vals)
        return vals
    
    def dfs(self, root, vals):
        if root:
            self.dfs(root.left, vals)
            self.dfs(root.right, vals)
            vals.append(root.val)
            

class Solution1:
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

# stack only solution
class Solution1:
    def postorderTraversal(self, root):
        stack = []
        result = []
        while root or stack:
            # traverse down left subtree
            while root:
                stack.append(root)
                root = root.left
            # no more in left subtree, set temp to last node's right child
            temp = stack[-1].right 
            # traverse down right subtree . threre is right subtree
            if temp:
                root = temp     # reassign root, continue while loop
            # no right subtree
            else:
                temp = stack.pop()
                result.append(temp.val)
                # while the popped node IS the right child of last on stack, pop & append
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
        return result
