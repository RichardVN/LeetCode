"""
https://leetcode.com/problems/subtree-of-another-tree/

TIME: O(NM)  where M is num nodes in Subtree

In English:  Subtree is in Main tree  if  there exists a Main-Subtree that is Same as Subtree
    - Create a isSame dfs helper that checks if two trees are same
    - check isSame(mainroot, subroot) ... if not check isSame(mainroot.children, subroot)

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # recurse
        if p and q:
            sameLeft = self.isSameTree(p.left, q.left)
            sameRight = self.isSameTree(p.right, q.right)
            if sameLeft and sameRight and p.val == q.val:
                return True
        return False 