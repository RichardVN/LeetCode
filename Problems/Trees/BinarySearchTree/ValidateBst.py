"""
Intuition:
    - A BST means we can traverse in INORDER dfs, and always be increasing
    - Recursive function for inorder dfs
        - Tree is valid if left and right subtree are valid
        - NOTE: instead of appending to vals array[], we can just have variable to hold
                single integer of last value
                    -> Return False if we are not greater than last value
                    -> Otherwise update last_value
        -> Return if left and right are valid TRUE

"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.last_value = - float("inf")
        
        # rtype: bool
        def valid(root):
            if not root:
                return True
            # left-> root -> right
            left_valid = valid(root.left)
            # process current, check if previous value was less than
            if self.last_value >= root.val:
                return False
            # update previous value
            else:
                self.last_value = root.val
            right_valid = valid(root.right)
            # return True or False up the tree
            return left_valid and right_valid
        
        # main function
        return valid(root)

"""
No return type
"""
class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        self.last_value = - float("inf")
        self.valid = True
        def dfs(current):
            if not current:
                return
            else:
                dfs(current.left)
                print(f"if {current.val} <= {self.last_value}")
                if current.val <= self.last_value:
                    print("INVALID")
                    self.valid = False
                else:
                    self.last_value = current.val
                dfs(current.right)
        dfs(root)
        return self.valid