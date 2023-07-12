"""
prob/subprob:
    - dfs(root) is valid iff dfs(root.left) and dfs(root.right) is valid

dfs approach
- Do NOT just compare root with child vals
- we need to know the L and R val boundaries of everything seen above

-> Returns bool is valid?
dfs (root, l_bound, r_bound)
    # base NONE -> valid
    # root.val out of bounds -> False
    # recursively check children

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