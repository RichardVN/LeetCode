# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import lru_cache
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # return List of unique BSTS ... repeated work!
        @lru_cache(None)
        def dfsGenerate(start, end):
            if start > end:
                return [None]
            
            trees = []
            for m in range(start, end + 1):
                leftTrees = dfsGenerate(start, m - 1)
                rightTrees = dfsGenerate(m + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(val=m, left=left, right=right)
                        trees.append(root)

            return trees
        
        return dfsGenerate(1, n)