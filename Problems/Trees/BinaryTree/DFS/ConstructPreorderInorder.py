# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""
for any preorder and inorder list:
    - Preorder  [ root,        [left subtree partition],       [right subtree partition] ]
    - Inorder    [ [left subtree partition],       root (mid),        [right subtree partition]]

1. Use first value in preorder to create TreeNode(root.val)
2. Use the root val to find the "mid" of inorder list
3. Use the "mid" of inorder to find the left (and right) partition sizes
4. Recursively build root.left and root.right using new preorder and inorder slices
    - Exclude first value of preorder
    - Exclude "mid" value of inorder
"""

class Solution:
    # hmap to retrieve index of mid in O(1) time
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # dfs returns root node ... and recursively builds into subtrees
        # params :  slice pointers for preorder and inorder. Lets us build subtree
        def dfs_build(pl, pr, il, ir):
            # Base: no preorder slice left to build
            if pl > pr or il > ir:
                return None
            
            rootval = preorder[pl]
            # root is the first value in preorder slice
            root = TreeNode(rootval)
            # find the mid value in inorder using hashmap
            mid = inorder_index_map[rootval]

            # calculate the partition sizes using mid
            left_partition_size = mid - il      # number of elements in [il, mid)
            preorder_split = pl + 1 + left_partition_size   # pl was processed, add 1.  preorder split is start of right subtree

            # recursively build subtrees TODO: we have used up FIRST item of preorder, and MIDDLE item of inorder
            root.left = dfs_build(pl + 1, preorder_split - 1, il, mid-1 ) 
            root.right = dfs_build(preorder_split, pr, mid+1, ir )

            return root

        # main
        inorder_index_map = {val:index for (index, val) in enumerate(inorder)}
        return dfs_build(0, len(preorder) - 1, 0, len(inorder) - 1)





  