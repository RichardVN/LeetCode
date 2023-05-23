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
        # dfs helper .. return UP  =>  (p_found, q_found)
        def dfs(root, p, q):
            # base 
            if not root: 
                return (False, False)
            # p_found iff ... at p, or p is in either subtree (recursive dfs)
            p_left, q_left = dfs(root.left, p, q)
            p_right, q_right = dfs(root.right, p, q)

            p_found = (root is p) or p_left or p_right
            q_found = (root is q) or q_left or q_right

            # TODO: do we have both? If lca not found yet, set as root
            nonlocal lca
            if p_found and q_found and lca is None:
                lca = root

            return (p_found, q_found)
        
        # LCA found at any point
        lca = None
        dfs(root, p, q)
        return lca