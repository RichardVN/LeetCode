class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1)]
        
        q = deque([(0, 0, 1)])
        visited = set()
        
        while q:
            r, c, distance = q.popleft()
            
            # invalid case:
            if (
                (r,c) in visited or
                r < 0 or
                c < 0 or
                r >= len(grid) or 
                c >= len(grid[0]) or
                grid[r][c] == 1
                
            ): 
                continue
            # success case:
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return distance
            
            print(r, c, distance)
            visited.add((r, c))
            
            for x, y in directions:
                nextR = r + x
                nextC = c + y
                q.append((nextR, nextC, distance + 1))
        
        return -1
        
        