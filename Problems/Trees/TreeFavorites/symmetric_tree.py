# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        s_left = [root.left]
        s_right = [root.right]
        
        while s_left and s_right:
            left_node = s_left.pop()
            right_node = s_right.pop()
            
            if not left_node or not right_node:
                if left_node != right_node:
                    return False
                else:
                    # dont check value of none, dont add its children
                    continue
            
            if left_node.val != right_node.val:
                return False
            
            # append no matter what(NONEs), catch identical (non mirror) sub trees
            # root, right, left
            s_left.append(left_node.left)
            s_left.append(left_node.right)
            
            # root, left, right
            s_right.append(right_node.right)
            s_right.append(right_node.left)
        # uneven nodes
        if s_left or s_right:
            return False
        return True
