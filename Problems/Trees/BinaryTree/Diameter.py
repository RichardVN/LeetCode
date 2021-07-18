"""
Recursive DFS approach:
    - What is the longest path/diameter thru a node?
        - Left depth + right depth
    - How do we get depths?
        - Postorder dfs traversal
    - how do return longest diameter inside dfs_depth method?
        - global variable diameter, updated within method

    
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # global var to keep track max variable
        self.diameter = 0
        # postorder traversal to get depths, dont need total depth
        _ = self.dfs_depth(root)
        
        return self.diameter
    
    """
    To caclulate path, we need depth of left subtree and right subtree
    We can use dfs_depth to traverse postorder to get depths
        --> BUT, the actual answer is sum of left depth and right depth, we update this variable
    """
    def dfs_depth(self, root):
        if not root:
            return 0
        left_depth = self.dfs_depth(root.left)
        right_depth = self.dfs_depth(root.right)
        
        # update global diameter if the sum of children is longest
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        return max(left_depth, right_depth) + 1