"""

Return Up :  NONE if val not found, or NODE that contains value
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            if root.val == val:
                return root # found value, return this node upwards
            # else we check children to see if they find value
            return dfs(root.left) or dfs(root.right)
            
        return dfs(root)