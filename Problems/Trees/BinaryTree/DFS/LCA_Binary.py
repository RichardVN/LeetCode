# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/editorial/
"""
1. Return?
        Main: Returns a TreeNode  NOTE: this occurs at specific node in tree, so we use global / nonlocal
        Helper: dfs returns upwards:  (seenP? and seenQ?)
2. Problem / subproblem
        Problem:  find LCA ... meaning  p_found AND q_found AND  lca was not set yet (is None)
        SubProblem: p_found  IFF
                        1. root IS p
                        2. p_found_left  (recursive call)
                        3. p_found_right (recursive call)
3. Base:
        NONE node  =>  (False, False).  Bottom of tree, so haven't seen p or q
4. Recurse:
        - Recurse into subtrees to see if p/q is found in subtrees rooted at node.left or node.right
        - AFTER, check if Node IS p or q
        - Check if found p, q, and first LCA

Time: O(N) to traverse nodes
Space: O(N)
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return (False, False)
            pfoundleft, qfoundleft = dfs(root.left)
            pfoundright, qfoundright = dfs(root.right)

            # boolean direct assignment : p_found iff ... root at p, or p is in either subtree (recursive dfs)
            pfound = root == p or pfoundleft or pfoundright
            qfound =  root == q or qfoundleft or qfoundright

            nonlocal lca
            # TODO: do we have both? If lca not found yet, set as root
            if lca is None and pfound and qfound:
                lca = root

            return (pfound, qfound)

        # global var cuz answer can occur at any node in tree
        lca = None
        dfs(root)
        return lca