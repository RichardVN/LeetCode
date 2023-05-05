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
        self.diameter = 0
        # This is longest diameter thru main root,
        _ = self.dfs_height(root)

        return self.diameter

    def dfs_height(self, node) -> int:
        if not node:
            return 0
        else:
            # value of node doesn't matter
            height_left = self.dfs_height(node.left)
            height_right = self.dfs_height(node.right)
            
            self.diameter = max(self.diameter, height_left + height_right)
            return max(height_left, height_right) + 1
