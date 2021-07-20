"""
Similar to Diameter of Binary Tree
INTUITION:
    - The max path sum does NOT need to pass thru root
        - we need global variable that is updated for max_path for any subtree state
        - for each root, need to consider if left and right branches make new max_path
        - Recursive function needs to return correct answer based on answer smaller subproblem
            - Calculate max path sum from root to leaf (similar max depth)

"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        # global var to keep track max variable
        self.max_path = root.val
        # postorder traversal to get max_paths
        self.dfs_sum(root)
        return self.max_path
    
    # RTYPE: integer, representing max_path_sum at a node max(left, right) + node
    # NOTE: very similar to diameter:  recursive function max_depth at node   max(left, right) + 1
    def dfs_sum(self, root):
        if not root:
            return 0
        # Recursive Case:  max at any node  =  NODE + subtree Sums if positive
                                # must include Node in case of single Negative Node
        # Important because we have NEGATIVE integers, and dont always want to include branches
        left = max(0, self.dfs_sum(root.left))
        right = max(0, self.dfs_sum(root.right))
        
        # TODO: Check if left AND right branches beat max at this state
        self.max_path = max(self.max_path, left+ right+ root.val)
        
        # return max path thru ONE branch and root
        return max(left, right) + root.val