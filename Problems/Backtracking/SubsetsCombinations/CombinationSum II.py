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