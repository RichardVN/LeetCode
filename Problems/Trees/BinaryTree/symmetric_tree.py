"""
NOTE: similar to SameTree except we compare different childs of root1 root2

Recursive Solution:
    - Base Case: Consider Two None (True), One None (False), Non-Non Dif Val (False)
    - Minimal Recursive Case:  Two Non-None nodes with none children, Outers mirrored / inner mirrored
    - Higher Recursive Case: Two Non-None nodes with Non-none children, outer / inner subtrees mirrored
    
"""
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.is_mirror(root.left, root.right)
    def is_mirror(self, left, right):
        # TODO: because we have no handling of None base case, need to consider left or right child none cases
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)


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
