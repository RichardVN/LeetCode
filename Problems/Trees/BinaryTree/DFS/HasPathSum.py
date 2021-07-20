"""
Intuition:
- DFS iterative
- Stack containing tuples (NODE, running_sum_at_node INCLUSIVE)
- if we ever process a node that is leaf AND current_sum == targetSum, return TRUE
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, 0)])
        
        while q:
            # process node
            node, current_sum = q.pop()
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                return True
            else:
                if node.right:
                    q.append((node.right, current_sum ))
                if node.left:
                    q.append((node.left, current_sum))
        # made thru entire tree
        return False

"""
Recursive solution:
    - on dfs, add additional parameter of current_sum so far
    - Each time we call dfs on a child, we add the childs value on current_sum
    - NOTE: also consider base case of left or right child is None
"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self.dfsPath(root, root.val, targetSum)
    def dfsPath(self, root, current_sum, targetSum):
        # NOTE: base case is leaf, not none
        if root.left is None and root.right is None:
            return True if current_sum == targetSum else False
        # Not leaf, but has one none children that we cant check .val
        if not root.left:
            return self.dfsPath(root.right, current_sum + root.right.val, targetSum)
        if not root.right:
            return self.dfsPath(root.left, current_sum + root.left.val, targetSum)
        # no none children
        return self.dfsPath(root.left, current_sum + root.left.val, targetSum) or self.dfsPath(root.right, current_sum + root.right.val, targetSum)
        