"""
CanSum with REPEAT USAGE of candidates
  --> dfs(i) instead of dfs(i+1) when we take item
"""


"""
Recursive Memoization

Time:  O(Target * N)   ,  for targetSum problems from [1, target] we have N decisions
Space: O(Target),  height of tree
"""
def canSum(target, nums): 
    # helper:  returns bool
    # i: item indices we are considring, remaining sum 
    def dfs(i, remaining):
        # check memo
        if remaining in memo:
            return memo[remaining]      #TODO: since we can take item multiple times, don't have to pass i as key

        # base: found answer
        if remaining == 0:
            return True
        # base: invalid states
        if remaining < 0 or i >= len(nums):
            return False
        # recursive decision ... take or not take item
        # take (TODO: can re-use any amt item i)      Do not use item i at all
        memo[remaining] = dfs(i, remaining - nums[i]) or dfs(i + 1, remaining)
        return memo[remaining]

        """  FOR LOOP VERSION
        for j in range(i, len(nums)):
            if dfs(j, remaining - nums[j]):
                memo[remaining] = True
                return True
        memo[remaining] = False
        return False
        """

    memo = {}
    # start with biggest problem "consider 0 through end"
    return dfs(0, target)



print(canSum(7 , [2,3])) # true
print(canSum(7 , [5,3,4,7])) # true
print(canSum(8 , [2,3,5])) # true


print(canSum(7 , [2,4])) # false
print(canSum(3000, [7,14])) # false



