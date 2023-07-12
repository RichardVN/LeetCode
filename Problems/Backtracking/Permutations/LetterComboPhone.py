"""
approach:
    - Similar to Combinations:  our base case is length of digits
    - we do NOT have a pop() backtrack case, because the Digit HAS to be used.  (not a Include/Exclude situation)

time:  O(4^N * N),  height of tree is N digits, branch x4 times each level
Space:  O(N),  length of digits and combo we are maintaining
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # implicit takes in combo
        def dfs(i, combo):
            if len(combo) == len(digits):
                combos.append(combo)
                return
            if i > len(digits):
                return
            # look thru all options
            for c in digitToChar[digits[i]]:
                dfs(i+1, combo + c)
            # TODO: we DO NOT have  to pop() because we DO NOT have a "do not take" case. we always use digit

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits: return []
        combos = []
        dfs(0, "")
        return combos