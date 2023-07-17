
"""
Same as Permutations I, but with duplicate inputs:
    - Counter for count of each num
    - RecursiveDecision Case:  append the Num if we have "remaining" Num to use (numCount > 0)

"""
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(perm) == len(nums):
                perms.append(perm[:])
                return
            # Decision, choose from available nums
            for num in numCounts:
                if numCounts[num] > 0:
                    # append using up a num
                    perm.append(num)
                    numCounts[num] -= 1

                    dfs()

                    # undo this decision
                    perm.pop()
                    numCounts[num] += 1

        perm = []
        perms = []
        # Map Num -> Count of num
        numCounts = Counter(nums)
        dfs()

        return perms