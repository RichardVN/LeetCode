"""
For any BST, realize that inorder traversal will process the values in SORTED order

Instead of processing values in list, we can just increment a "global" index value

Time: O(N) dfs traversal
Space: O(N) to stack, but no array created

"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            nonlocal index
            nonlocal res
            if root:
                dfs(root.left)
                index += 1          # TODO: instead of vals.append(root.val), just keep track of "index"
                if index == k:      # Technically this is still O(N) due to call stack
                    res = root.val
                dfs(root.right)
        index = 0
        res = None
        dfs(root)
        return res