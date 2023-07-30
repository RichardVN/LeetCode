"""
Unlike backtracking where we add to path and then dfs() call, 
we wait to see if dfs() returns non-None before appending nums[i]

Time:  target^2 * N , N is number branchesk
Space:  target^2 , target is height of tree
"""
def shortestSum(target, nums):
    def shortestCombo(i, remainder):
        if remainder in memo:
            return memo[remainder]
        # base smallest subproblem
        if remainder == 0:
            return []
        # base invalid
        if remainder < 0:
            return None

        # recursive decision
        shortest = None
        for j in range(i, len(nums)):
            # take at j
            remainderCombo = shortestCombo(j , remainder - nums[j])
            if remainderCombo is not None:
                thisCombo = remainderCombo + [nums[j]]
                if not shortest or len(thisCombo) < len(shortest):
                    shortest = thisCombo
        memo[remainder] = shortest
        return memo[remainder]


    memo = {}
    return shortestCombo(0, target)

print(shortestSum(7 , [5,3,4,7])) # [7]
print(shortestSum(8 , [1,4,5])) # [4,4]
# print(shortestSum(10000 , [1,4,5])) # [4,4]

