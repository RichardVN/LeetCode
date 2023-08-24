
"""
We are finding ANY path ... not all paths (which would require backtracking)  ... 

# TODO: non-directional graph. When traversing, make sure to not traverse back to parent.
1. Mark visited Nodes with set 'visited'
2. Create a hash map of Neighbor Lists  using input edges
3. dfs(node) Helper:  add node to visited. iterate thru each neighbor and dfs
4. Call dfs(source) in main code

"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # return upwards if we found destination
        def dfs(node):
            if node in visited:
                return False
            if node == destination:
                return True

            # add visited to set so we dont backtrack (careful since we are undirected graph)
            visited.add(node)
            neis = neighbors[node]
            for nei in neis:
                isFound = dfs(nei)
                # if we found ANY valid path we can immediately return... else continue looking thru neighbors
                if isFound:
                    return True
            return False
        
        # create map of node to neighbors. Anytime key is not in dict, we just return []
        neighbors = defaultdict(list)

        # undirected, 2 directional
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # dfs traversal from source node, see if destination is reachable
        visited = set()
        return dfs(source)

"""
BFS using queue solution
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # preprocessing into map of node: neighbor list[]
        neighbors = defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        print(neighbors)
        
        toVisit = deque([source])
        visited = set()
        
        while toVisit:
            node = toVisit.popleft()
            # TODO: perform this check AFTER popping ... not before adding to queue 
            if node in visited: 
                continue
            visited.add(node)
            
            if node == destination:
                return True
            for nei in neighbors[node]:
                toVisit.append(nei)
            
        return False