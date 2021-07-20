"""
Recursive solution:
    - base case:   Height of None node returns 0
        - NOTE: Return -1 if depth of single node considered 0
    - Minimal Recursive case:   Height of a node with None children is 1 
    - High Recursive case:  height of node with non-none children is max(children_depth) + 1
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        return self.dfs(root)
    
    def dfs(self,root):
        # TODO: because we handle None base case, we don't need base case for left or right child is none
        if not root:
            return 0
        # Post-order implementation, visit left subtree -> right subtree -> compute depth at ROOT
        left_subtree_depth = self.dfs(root.left)
        right_subtree_depth = self.dfs(root.right)
        return max(left_subtree_depth, right_subtree_depth) + 1

"""
Iterative DFS using stack
    - push tuple of NODE, current_height
    - if leaf check if new max height
"""
    
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        # iterative bfs
        # stack of node, height at node
        best_height = 0
        
        if not root:
            return 0
        s = [(root, 1)]
        
        while s:
            node, current_height = s.pop()
            # if leaf node
            if not node.left and not node.right:
                best_height = max(best_height, current_height)
            if node.right:
                s.append((node.right, current_height + 1))
            if node.left:
                s.append((node.left, current_height+1))
        return best_height
