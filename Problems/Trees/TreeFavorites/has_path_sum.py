# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # maintain a stack of node and current_sum so far including that node
        q = deque([(root, root.val)])
        
        while q:
            node, current_sum = q.pop()
            if not node.left and not node.right and current_sum == targetSum:
                return True
            else:
                if node.right:
                    q.append((node.right, current_sum + node.right.val))
                if node.left:
                    q.append((node.left, current_sum+node.left.val))
        # made thru entire tree
        return False