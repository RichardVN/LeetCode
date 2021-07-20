"""
What does inorder and postorder tell us?
    - Postorder is Left Tree -> Right Tree -> Root
        - The ROOT is always processed last
        - Left Tree values before Right tree values, of some size partition
    - Inorder is Left Tree -> Root -> Right Tree
        - Values LEFT of root is left subtree, values RIGHT of root is right subtree
Procedure:
    - Recursive function (inorder, postorder)  -> Node
    - Base case: inorder or postorder empty list []
    - Recursive Case: non empty list
        # make Node by popping value
        1. Take last value from postorder
        2. Make a TreeNode using Value
        # recursively build child nodes with adjusted lists
        3. find index of value in inorder
            a. partition inorder on either side of middle_index
            b. parition postorder (excluding popped element), by size of partitions
        4. Array goes left-> right -> ROOT, we built root so build right first

"""

class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        # base case, empty lists
        if not inorder or not postorder:
            return None
        # take last item from postorder as root
        value = postorder[-1]
        
        # make a node
        root = TreeNode(value)
        
        # we just built ROOT(right value), values next to root is RIGHT subtree
        mid_idx = inorder.index(value)
        
        root.right = self.buildTree(inorder[mid_idx+1:],postorder[mid_idx:-1] )
        root.left = self.buildTree(inorder[:mid_idx] , postorder[:mid_idx])
        
        return root
    
"""
What does inorder and postorder tell us?
    - Postorder is Left Tree -> Right Tree -> Root
        - The ROOT is always processed last
        - Left Tree values before Right tree values, of some size partition
     Inorder is Left Tree -> Root -> Right Tree
        - Values LEFT of root is left subtree, values RIGHT of root is right subtree
Procedure:
    - Recursive function (inorder, postorder)  -> Node
    - Base case: inorder or postorder empty list []
    - Recursive Case: non empty list
        # make Node by popping value
        1. Take last value from postorder
        2. Make a TreeNode using Value
        # recursively build child nodes with adjusted lists
        3. find index of value in inorder
            a. partition inorder on either side of middle_index
            b. parition postorder (excluding popped element), by size of partitions
        4. Array goes left-> right -> ROOT, we built root so build right first

"""

class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        # base case, empty lists
        if not inorder or not postorder:
            return None
        # take last item from postorder as root
        value = postorder[-1]
        
        # make a node
        root = TreeNode(value)
        
        # we just built ROOT(right value), values next to root is RIGHT subtree
        mid_idx = inorder.index(value)
        
        root.right = self.buildTree(inorder[mid_idx+1:],postorder[mid_idx:-1] )
        root.left = self.buildTree(inorder[:mid_idx] , postorder[:mid_idx])
        
        return root
    
"""
What does inorder and preorder tell us?
    - Preorder is Root ->  Left Tree -> Right Tree 
        - The ROOT is always processed First
        - Left Tree values before Right tree values, of some size partition
    - Inorder is Left Tree -> Root -> Right Tree
        - Values LEFT of root is left subtree, values RIGHT of root is right subtree
Procedure:
    - Recursive function (inorder, preorder)  -> Node
    - Base case: inorder or preorder empty list []
    - Recursive Case: non empty list
        # make Node by popping value
        1. Take first value from preorder
        2. Make a TreeNode using Value
        # recursively build child nodes with adjusted lists
        3. find index of value in inorder
            a. partition inorder on either side of middle_index
            b. parition preorder (excluding popped element), by size of partitions
        4. Array goes Root -> left -> right, we popped root so build left next

"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        # preorder is Root -> left -> right
        value = preorder[0]
        root = TreeNode(value)
        
        # find index of inorder
        mid = inorder.index(value)
        
        root.left = self.buildTree(preorder[1:mid+1] , inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:] , inorder[mid+1:])
        
        return root