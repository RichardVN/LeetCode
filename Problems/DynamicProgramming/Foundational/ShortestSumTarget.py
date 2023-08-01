"""
Unlike backtracking where we add to path and then dfs() call, 
we wait to see if dfs() returns non-None before appending nums[i]

Time:  target^2 * N , N is number branchesk
Space:  target^2 , target is height of tree
"""
def shortestSum(target, nums):
    def dfs(i, remainder):
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
            remainderCombo = dfs(j , remainder - nums[j])
            if remainderCombo is not None:
                thisCombo = remainderCombo + [nums[j]]
                if not shortest or len(thisCombo) < len(shortest):
                    shortest = thisCombo
        memo[remainder] = shortest
        return memo[remainder]


    memo = {}
    return dfs(0, target)

def shortestSum1( target , nums):
    # "what is shortest combo, for given i and target?"
    def dfs(i, target):
        # success
        if target == 0:
            return []
        # invalid
        if i >= len(nums) or target < 0:
            return None
        
        shortest = None
        # recursive decisions
        # take 
        take = dfs(i, target - nums[i])
        if take is not None:
            take.append(nums[i])
            shortest = take if not shortest or len(take) < len(shortest) else shortest
        # or skip
        skip = dfs(i+1, target)
        if skip is not None:
            shortest = skip if not shortest or len(skip) < len(shortest) else shortest

        # return shortest for this subproblem
        return shortest

        

    return dfs(0, target)

print(shortestSum1(7 , [5,3,4,7])) # [7]
print(shortestSum1(8 , [1,4,5])) # [4,4]
# print(shortestSum(10000 , [1,4,5])) # [4,4]

