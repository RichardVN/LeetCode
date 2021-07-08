"""
LEFT --> ROOT --> RIGHT
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vals = []
        self.dfs(root, vals)
        return vals
        
    # in order:  left -> root -> right
    def dfs(self, root, vals):
        # if root to make sure we not at end NONE base case
        if root:
            self.dfs(root.left, vals)
            vals.append(root.val)
            self.dfs(root.right, vals)

# iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        """NOTE: we have to check root, sometimes stack empty not done traversal"""
        while stack or root:
            # go as far down left as we can
            if root:
                stack.append(root)
                root = root.left
            # we have reached end of left subtree
            else:
                # cant go further, pop latest from stack
                tmpNode = stack.pop()
                # append node's value
                ans.append(tmpNode.val)
                # reassign root from None to the popped Node's right subtree
                root = tmpNode.right

        return ans
            