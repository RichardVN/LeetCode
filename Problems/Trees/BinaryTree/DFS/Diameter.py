"""
TODO KEYS:
- height of Node = max(height left, height right) + 1
- diameter THRU Node = height left + height right

- TODO: diameter does not necessarily go through main root
    - it can occur "anywhere" in tree. -> we must use a global variable
      variable that tracks longest diameter
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # returns up depth of tree
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            # recurse to find depth subtrees
            depth_left = dfs(root.left)
            depth_right = dfs(root.right)

            #calc diameter and update
            diameter = max(depth_left + depth_right, diameter)

            depth = max(depth_left, depth_right) + 1
            return depth
        
        diameter = 0
        dfs(root)
        return diameter