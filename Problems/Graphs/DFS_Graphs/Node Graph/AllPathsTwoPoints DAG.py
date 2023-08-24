"""
DIRECTED graph. No 'visited' set needed
"""

"""
Recursive DFS solution
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node == len(graph) - 1 :
                paths.append(path.copy())
                return
            
            # dfs thru decisions ... NOTE: similarity to subsets I structurex
            for nei in graph[node]:
                # Take decision
                path.append(nei)
                # Recursively call given this decision
                dfs(nei)
                # undo decision
                path.pop()
            
        
        paths = []
        path = [0] # TODO: we need to initialize our path with start node
        
        dfs(0)
        
        return paths

"""
Iterative DFS solution

Add (node, path) to the stack or queue
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # (node, path)
        result = []
        s = [(0, [0])]
        target = len(graph) - 1
        
        while s:
            node, path = s.pop()
            if node == target:
                result.append(path)
            else:
                for nei in graph[node]:
                    s.append((nei, path+[nei]))
        
        return result