"""
DIRECTED graph with NO CYCLE -> No 'visited' set needed


Same Complexities as Subset I
Time:   2^V * V    ... backtracking, take or skip choice for V vertices  *  Space to copy
Space:  O(V) ... size recursive stack

"""

"""
Recursive DFS solution
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            # base
            if node == len(graph) - 1:
                paths.append(path.copy())
            
            # recursive 
            for nei in graph[node]:
                # decision
                path.append(nei)
                # recursive dfs ... take, dfs , undo
                dfs(nei)
                # undo
                path.pop()
        
        paths = []
        path = [0] # TODO: we start from source node
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