"""
Time: 
"""
from collections import deque
class Solution1:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        root3 = TreeNode(-1)
        root3 = self.dfs_merge(root1, root2, root3)
        return root3
    
    def dfs_merge(self, root1, root2, root3):
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        
        root3 = TreeNode(root1.val + root2.val)
        root3.left = self.dfs_merge(root1.left, root2.left, root3.left)
        root3.right = self.dfs_merge(root1.right, root2.right, root3.right)
        return 
    
"""
Recursive Solution:
    - Base Case:
        - Either root1 or root2 is None, return the other
    - Recursive Case (both root1 and root2):
        - add root1 and root2 vals as new root1 val
        - call merge on left childs and right childs
        - return root1
"""
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs_merge(root1, root2):
            # if both none, then returning root2 would be none
            if not root1:
                return root2
            if not root2:
                return root1
            # both roots have values, merge
            root1.val = root1.val + root2.val 
            # recursively go deeper
            root1.left = dfs_merge(root1.left, root2.left)
            root1.right = dfs_merge(root1.right, root2.right)
            return root1
        merged_root = dfs_merge(root1, root2)
        return merged_root