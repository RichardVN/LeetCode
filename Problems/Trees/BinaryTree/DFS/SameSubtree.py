"""
Given Tree S and and SubTree T
Traverse all node in s:
    check if subtree starting at Node equals sub tree T
Time: Go thru N nodes, and M nodes in subtree, O(N * M)
"""
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs_compare(root, subroot):
            stack1 = [root]
            stack2 = [subroot]
            
            while stack1 and stack2:
                node1 = stack1.pop()
                node2 = stack2.pop()
                
                # if both None
                if not node1 and not node2:
                    continue
                # if one none
                if not node1 or not node2:
                    return False
                # both have values
                if node1.val != node2.val:
                    return False
                
                # equal values, append children
                stack1.append(node1.right)
                stack1.append(node1.left)
                
                stack2.append(node2.right)
                stack2.append(node2.left)
            if stack1 or stack2:
                return False
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                equal = dfs_compare(node, subRoot)
                if equal:
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False