"""
BST definition:  for a node.val, ALL nodes in right subtree need to be strictly greater
    - We can’t just compare children with parent. 
    - Need to have left_boundary and right_boundary.. 

Create a dfs helper that returns upwards whether the subtree is valid
Pass DOWN: the next root to check, l_bound, r_bound
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, l_bound, r_bound):
            # base .. None node is valid
            if not root: return True

            # process this node TODO: BST can NOT have equal values
            if not (root.val > l_bound and root.val < r_bound):
                return False

            # this tree valid IFF subtrees are valid
            # root.val acts as new left or right bound, depending on direction 
            return dfs(root.left, l_bound, root.val) and dfs(root.right, root.val, r_bound)       # bool, returns True or False upwards

        res = dfs(root, -float("inf"), float("inf"))
        return res