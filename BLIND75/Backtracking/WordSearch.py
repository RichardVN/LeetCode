"""
Intuition. Call dfs starting on every square

dfs
    - Base:
        if we hit the length of word return true
        if we outside bounds or NOT match character, or on SEEN node, return False
    - Recursive:
        add matching letter r,c to seen
        recursive calls on adjacent squares
        Remove r,c from seen

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # note just modify, need to return UPWARDS!
        def dfs(r,c, i, seen):
            # found enough matching letters
            if i == len(word):
                return True
            # base case
            if r<0 or c<0 or r >=R or c >=C or board[r][c] != word[i] or (r,c) in seen:
                return False
            # Found matching. Add to seen set, further recursive calls with i+1
            seen.add((r,c))
            res = (dfs(r+1,c, i+1, seen) or
                dfs(r-1,c, i+1, seen) or
                dfs(r,c+1, i+1, seen) or
                dfs(r,c-1, i+1, seen) )
            seen.remove((r,c)) # if we hit dead end
            return res
        # main shell
        
        if not board:
            return False
        R = len(board)
        C = len(board[0])
        
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0, set()):
                    return True
        return False