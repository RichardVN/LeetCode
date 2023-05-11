"""
what return up?
    - bool AND depth of tree
Problem:
- Is Tree height balanced
Sub Problem:
- Tree balanced iff difference depth_left and depth_right < 2

Base:
- No Root -> 0, True
Recursive:
- Root, l and R ...
    - recurse into l and r for depths. 
    - calculate difference and return answer (depth, balanced?)
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we need send height, bool upwards
        def dfs_balanced(root):
            if not root: return (0, True)

            l_depth, l_balanced = dfs_balanced(root.left)
            r_depth, r_balanced = dfs_balanced(root.right)
            this_balanced = l_balanced and r_balanced and (abs(r_depth - l_depth) < 2)
            return (max(l_depth, r_depth) + 1, this_balanced)

        # TODO: the dfs_helper is returning a tuple
        depth, balanced = dfs_balanced(root)
        return balanced