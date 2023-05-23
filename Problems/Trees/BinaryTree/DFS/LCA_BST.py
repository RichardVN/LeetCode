# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
NOTE: We have p.val and q.val
TODO: The key is that the LCA is the FIRST node we encounter where
    1. p.val and q.val are NOT both greater
    2. p.val and q.val are NOT both less
BST:
- we know at Node N ...
    - Values greater than N.val are in right subtree
    - Values less than N.val are in left subtree
Pseudo:
    - Similar to Binary search
    WHILE CURR
    - If both p and q less, go left
    - If both p and q more, go right
    - Else: this is LCA

Time: O(N)
Space: O(N) for skewed bst
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        # step through with pointer while it is not None
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr