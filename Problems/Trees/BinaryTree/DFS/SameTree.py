"""
NOTE: similar to SymmetricTree except we compare different childs of root1 root2

Recursive DFS:
Base case:
    - None and None  -> True
    - None and Not None -> False
    - Not None and Not None, different values -> False
Recursive case:
    - Not None and Not None , sanme values
    - Return True if lefts are same and rights are same

"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # recursive dfs --> boolean
        def dfs_same(root1, root2):
            if not root1 and not root2:
                return True
            # one is none but not both
            if not root1 or not root2:
                return False
            # neither is none
            if root1.val != root2.val:
                return False
            # Recursive case. Two nodes with equal values
            return dfs_same(root1.left, root2.left) and dfs_same(root1.right, root2.right)
        
        return dfs_same(p, q)