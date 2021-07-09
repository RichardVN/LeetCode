# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
""" Recursive dfs solution """
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res
        
    def dfs(self, root):
        if not root:
            return 0
        else:
            return (1+ max(self.dfs(root.left), self.dfs(root.right)))
        
""" Iterative BFS level by level solution """
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque([root])
        height = 0
        # outer loop over each level:
        while q:
            height += 1
            level_length = len(q)
            # Inner loop over nodes in level, append children:
            # for loop to ensure we dont travers the children we just added
            for _ in range(level_length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return height
            
""" Iterative dfs, pass running sum thru tuple"""
class Solution:
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
        