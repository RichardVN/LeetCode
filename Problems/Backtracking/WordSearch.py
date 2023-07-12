"""
KEYS:
    - create a set()  for  path of (r,c) letters visited
    - path.remove()  after  4 dfs calls into adjacent cells 
    - dfs() calls after backtrack is NOT necessary  ... (not working with combination/subset)

    
Decision Tree:
    - after choosing letter: we have 3 decision paths
    - we can choose letter up to len(word)

Time: O(3^L  *  N)   N is cells on board, L is length of word
Space: O(L)          size of path set to

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # TODO: do not repeat a square
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)
