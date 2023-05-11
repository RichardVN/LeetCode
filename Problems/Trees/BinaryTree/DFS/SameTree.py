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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p ,q) -> bool:
            # base
            if not p and not q:
                return True
            # one but not the other
            if not (p and q):
                return False
            if p.val != q.val:
                return False

            # recursive: True if (check subtrees, left and right are same)
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)