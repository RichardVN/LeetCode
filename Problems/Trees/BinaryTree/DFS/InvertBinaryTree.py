"""
https://leetcode.com/problems/invert-binary-tree/description/
What to return?
    - Void ..  just traverse and swap
Problem and subproblem:
    - problem is invert tree
    - Subproblem: have to invert left sub tree, and right subtree
Base (we can answer directly):
    - root is None:
        return
recursive:
    - has ONE or both of left / right:
        - swap
        - recurse into subtrees and invert

Time: O(N)
Space: O(N)

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_invert(root):
            if not root:
                return
            # process for this node
            root.left, root.right = root.right, root.left
            # now we have to recurse into subtree and invert
            dfs_invert(root.left)
            dfs_invert(root.right)

        if not root: return None

        dfs_invert(root)

        return root