"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root])
        levels = []
        
        while q:
            levelSize = len(q)
            level = []
            
            for _ in range(levelSize):
                node = q.popleft()
                level.append(node.val)
                q.extend(node.children) # TODO:  append children to queue
            
            levels.append(level)
        
        return levels