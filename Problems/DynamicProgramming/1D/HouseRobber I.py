"""
Recursive relation: memo[i] = max(memo[i-1], nums[i] + memo[i-2]) 

" at any house i ... decide whether to rob and add to (i-2) profits, or skip and take (i-1) profits "

Time: O(N) because we solve subproblem up to N houses at most once before caching
Space: O(N) for call stack tree height, and memo
"""
# 1. Top-Down recursive memoization cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
            # base cases: outside of bounds
            if i < 0 :
                return 0
            # Cache subproblem. rob house or not rob house
            memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
            return memo[i]

        memo = {}
        return dfs(len(nums) - 1)
    
    def rob2(self, nums: List[int]) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
            # base cases
            if i >= len(nums) :
                return 0
            # Cache subproblem. rob house or not rob house
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        memo = {}
        return dfs(0)
    
# 2. Bottom Up - Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        # trivial case
        if len(nums) <= 2:
            return max(nums)

        memo = [0 for _ in range(len(nums))]
        # base subproblem:
        memo[0] = nums[0] # only considering first house
        memo[1] = max(nums[1], nums[0]) # we took from 1st house or 2nd

        # cache subproblems PAST base:
        for i in range(2, len(memo)):
            # if we rob from i house, we could not have taken from i - 1 house
            memo[i] = max(memo[i-1], nums[i] + memo[i-2]) 
        return memo[-1]

# 2b. Iteration with limited variable caching
class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize vars for previous subproblem answers
        prev1, prev2 = 0, 0

        for n in nums:
            curr = max(n + prev2, prev1) #TODO: recursive relation

            # update prev caches
            prev2 = prev1
            prev1 = curr
        return curr