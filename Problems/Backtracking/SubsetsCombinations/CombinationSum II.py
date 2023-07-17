class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, total):
            if total == target:
                combos.append(combo[:])
                return
            if i >= len(candidates) or total > target:
                return
            # decisions
            combo.append(candidates[i])
            dfs(i+1, total + candidates[i])
            combo.pop()
            # TODO: skip going over dupe
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            dfs(i+1, total)
        

        # TODO: input has dupes. we have to handle those
        candidates.sort()
        combo, combos = [],[]
        # dfs thru candidates i
        dfs(0, 0)
        return combos

"""
Alternate solution with for loop:
- Base cases
    - when to append (total == target)
    - stop exploration (total > target)
- For loop decision tree, bounds indices for us
    - Skip over duplicate inputs, if j is NOT at the first instance of input
    - Make sure to increment total, when recursively calling dfs
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, total):
            if total == target:
                combos.append(combo[:])
                return
            if total > target:
                return
            for j in range(i, len(candidates)):
                # just popped, skip dupes
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                combo.append(candidates[j])
                # we increment j, cannot use one "index" of input twice
                dfs(j+1, total + candidates[j])
                combo.pop()

        # input has dupes. we have to handle those
        candidates.sort()
        combo, combos = [],[]
        # dfs thru candidates i
        dfs(0, 0)
        return combos