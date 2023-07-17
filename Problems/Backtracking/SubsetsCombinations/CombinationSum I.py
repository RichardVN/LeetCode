"""
NOTE: This decision tree is more similar to subset question .. Combinations can be different lengths
2-way decision tree:
    - Take or NOT take num
    - we can take num multiple times
    - ex. left subtree contains all subset that HAVE to contain X copies of num

There is no limit to dupes or combo length... just limited by target
Time: O(2^T) where T is target value
Space: O(T) ... worst case where our only candidate is smallest integer 1

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # must add to target. Pass down total sum so far
        def dfs(i, total):
            # Base ... append when we have reached target
            if total == target:
                combos.append(combo[:])
                return
            # invalid i or invalid total
            if total > target or i >= len(candidates):
                return
            # decision tree
            combo.append(candidates[i])
            # TODO: we keep duping this candidate until base case
            dfs(i, total + candidates[i])
            # our first pop is when we are at first valid i
            combo.pop()
            # we can now explore other candidates. Total has NOT changed since we did not take
            dfs(i+1, total)

        combo, combos = [], []
        # first valid candidate at index 0
        dfs(0, 0)
        return combos
    

"""
Alternative solution using for loops:
- For loops still keeps us in valid indices
- Additional base cases:
    - when to append combo (total == target)
    - when to stop exploring (total > target)
"""    
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # must add to target. Pass down total sum so far
        def dfs(i, total):
            # Base append ..
            if total == target:
                combos.append(combo[:])
            if total > target:
                return
            # candidates are always the same... only total limits
            for j in range(i, len(candidates)):
                combo.append(candidates[j])
                # TODO: instead of j + 1, we can repeat the current number
                dfs(j, total + candidates[j])
                # its only at this point, we can proceed j to another candidate
                combo.pop()


        combo, combos = [], []
        # first valid candidate at index 0
        dfs(0, 0)
        return combos