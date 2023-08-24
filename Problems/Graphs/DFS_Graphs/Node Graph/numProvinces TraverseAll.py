"""
Similar to numIslands:
1. Go thru each Node / Cell.  
2. If Node / Cell is not in visited, increment island and start dfsTraversal
3. dfsHelper:
        add Node / Cell to visited and call dfs on neighbors

TODO:  to go through each "node" of an adjacency matrix graph, we just go row by row
        to go through each "neighbor" of a node, we go to each cell in the row if it is NOT a 0 value
We are given an adjacency matrix with N nodes  (0, 1, 2 ...)

"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # helper to mark node as seen, and recursively dfs thru neighbors
        def dfs(node):
            if node in visitedNodes:
                return
            # node is now visited
            visitedNodes.add(node)
            # dfs thru other connected nodes
            for nei in range(numNodes):
                if isConnected[node][nei] == 1:
                    dfs(nei)

        numNodes = len(isConnected)
        distinctComponents = 0

        visitedNodes = set()

        # For each node, if we have not visited node yet: start a dfs from node
        for node in range(numNodes):
            if node not in visitedNodes:
                distinctComponents += 1
                dfs(node)


        return distinctComponents