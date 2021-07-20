"""
INTUITION:
    - dfs recursive calls DOWN the tree
    - Base case push return values back UP tree
    
APPROACH:
    Recursive DFS algorithm, return BOOL type
    - 1. Traverse from root node
    - 2. If current is p or q, then overlap is True
    - 3. Recurse calls on left and right branch, finding p or q
    - 4. If at any point, two of flags are true, That is LCA, since we come bottom up
            -> Update global variable

Recursively call down tree, return answer bottom - up
Answer :  what is lowest common ancestor node
Recrse function:  has p or q been found yet?

Base Case:
    - If None node, return [p_found, q_found] aka. [False, False]
Recursive Case:
    - Recursively call dfs on children, to see if p or q found in left or right subtree
    - Process current node. Is current.val == p.val or q.val??
    - UPDATE ANSWER GLOBAL
    - Return [p_found, q_found]

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs_recurse(root):
            # base case:  if single NONE node, then neither p or q found
            if not root:
                return [False, False]

            # recursive calls on children
            left_p_found, left_q_found = dfs_recurse(root.left)
            right_p_found, right_q_found = dfs_recurse(root.right)

            # Process current Node
            p_found = left_p_found or right_p_found or root.val == p.val
            q_found = left_q_found or right_q_found or root.val == q.val

            # Conditions met (both p and q found), only update if no answer yet
            if p_found and q_found and self.LCA is None:
                self.LCA = root

            # return upwards the answer
            return [p_found, q_found]
        
        # global variable to be updated when conditions met in tree
        self.LCA = None
        dfs_recurse(root)
        return self.LCA
    