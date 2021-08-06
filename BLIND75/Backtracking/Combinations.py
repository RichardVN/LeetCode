"""
We start with empty array []  with all candidates from 1 thru N

- Base:  we reach length k and append the combination
- Recursive: current representing candidates chosen so far, start representing start of candidates remaining
    - we Loop thru each candidate
    - we append candidate
        -> We recursive call (current + candidate, shifted_start_idx)

Time:  K  *  N Choose K 
Space: N choose K,   N! / K! (N-k)!
"""


class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(current, start):
            if len(current) == k:
                res.append(current[:])
                return
            # recursive
            for i in range(start, n+1):
                backtrack(current + [i], i+1)
        # shell
        res = []
        backtrack([], 1)
        return res

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(current, start):
            if len(current) == k:
                res.append(current[:])
                return
            # Loop over all possible decisions
            for i in range(start, n+1):
                # make decision
                current.append(i)
                # recursive call with the decision we made
                backtrack(current, i+1)
                # undo decision. Skip choosing this i
                current.pop()
        # shell
        res = []
        backtrack([], 1)
        return res
