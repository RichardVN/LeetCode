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

            # look thru all options for our given i
            for c in digitToChar[digits[i]]:
                # pick candidate c 
                combo += c
                # dfs call with remaining candidates and updated i
                dfs(i+1, combo)
                # we have reached base case, pop our candidate pick and iterate to next candidate
                combo = combo[:-1]

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