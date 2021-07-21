"""
Keep track of level number
If level number is odd, reverse level_array before appending
"""
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(root):
            q = deque([root])
            level_number = 0
            # while loop while there is node in queue
            while q:
                level_size = len(q)
                # value array for this level
                level_vals = []
                # go thru each node in level
                for i in range(level_size):
                    node = q.popleft()
                    level_vals.append(node.val)
                    # append children if not none
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                # reverse array if odd level number
                if level_number % 2 != 0:
                    level_vals.reverse()
                # append level array to main array
                result.append(level_vals)
                # update level number
                level_number += 1
                
        # TODO: EMPTY TREE CASE
        if not root:
            return []
        
        result = []
        # fill result array
        bfs(root)
        
        return result