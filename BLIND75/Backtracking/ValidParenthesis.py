"""
    open_count: 
    close_count:
    
We can only add closing parenthesis if close_count < open_count

Back Track:
    - Base:
        - 3 open, 3 close
        - add to combination to result
    - Recursive:
        - Decision 1: add closing if close < open, increment close
        - Decision 2: add open if open > 3, increment open
        
Time: Branch (base) ^ Depth
    - b = branches per node
    - d = max depth recursion tree
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(current, open_count, close_count):
            if open_count == n and close_count == n:
                res.append(current)
                return
            if close_count < open_count:
                dfs(current +")", open_count, close_count + 1)
            if open_count < n:
                dfs(current +"(", open_count + 1, close_count)
        res = []
        dfs("", 0, 0)
        return res