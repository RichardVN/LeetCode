"""
https://leetcode.com/problems/subtree-of-another-tree/

TIME: O(NM)  where M is num nodes in Subtree

For each node in Tree, call SameTree on p, q

1. Write helper for SameTree(p,q)
2. write isSubtree(p,q)
    - q from SUBTREE is always passed down
    - Subproblem:  existsSubtree if existsSubtree(L or R)
    - base: 
        if subtree root NONE =>  True, existsSubtree
        if tree root NONE => False
        if SameTree(p,q) => True
    - Recursive:
        no subtree found, recurse deeper
        existsSubtree(L) OR existsSubtree(R)

"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs_same(p, q):
            # if both None, it is same
            if not p and not q:
                return True
            # recurse into children to find answer
            if p and q and p.val == q.val:
                return dfs_same(p.left, q.left) and dfs_same(p.right, q.right)
            return False

        # q is subtree root, always used as comparison
        def dfs_subtree(p,q):
            # base cases
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif p and not q: 
                return True
            
            # Use helper for current roots. Recurse over subtree from this node and compare.
            if dfs_same(p, q):
                return True
            # no subtree found yet. Recurse deeper to send up answer.
            return dfs_subtree(p.left, q) or dfs_subtree(p.right, q)

        return dfs_subtree(root, subRoot)
