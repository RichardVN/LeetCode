"""
Iterative Stack dfs:
    - push Node, Current depth to stack
    - If pop leaf node, check value and update min depth so far
"""
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # (node, height at node)
        stack = [(root, 1)]
        min_depth = float("inf")
        while stack:
            node, current_depth =  stack.pop()
            # TODO: after pop, check if this is leaf node
            if not node.left and not node.right:
                min_depth = min(min_depth, current_depth)
            
            if node.right:
                stack.append((node.right, current_depth + 1))
            if node.left:
                stack.append((node.left, current_depth + 1))
        return min_depth
"""
NOTE:  minimum depth to LEAF node. None nodes do not count
        ex. root with no left but long right, count right
        --> WE HAVE to include more base cases if left child or right child is none
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs_min(root):
            if not root:
                return 0
            if not root.left:
                return dfs_min(root.right) + 1
            if not root.right:
                return dfs_min(root.left) + 1
            return min(dfs_min(root.left) , dfs_min(root.right)) + 1
        if not root:
            return 0
        return dfs_min(root)