"""
All Combos ... -> backtracking, 2^N
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opening, closing):
            # successful base TODO: we need combo of certain length n
            if opening == n and closing == n:
                combos.append("".join(combo))
            # invalid base
            if closing > n or opening > n:
                return

            # make decisions, recurse deeper
            # are we able to add a valid closing?
            if opening > closing:
                combo.append(')')
                dfs(opening, closing + 1)
                combo.pop()
            # we can always append open
            combo.append('(')
            dfs(opening + 1, closing)
            combo.pop()
            

        
        combo, combos = [], []

        dfs(closing=0, opening=0) # until n reached

        return combos

