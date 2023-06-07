# https://leetcode.com/problems/binary-tree-right-side-view/
"""
BFS
- level order traversal
- if we are on last item of level, append to res

Time: O(N)
Space:O(N)
"""

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        # while q ... append level
        while q:
            level_size = len(q)
            for i in range(level_size):
                # pop front of q
                node = q.popleft()
                # if this is last item in level,m append to res
                if i == level_size - 1:
                    # NOTE: append val and not node itself
                    res.append(node.val)
                # append children if exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res