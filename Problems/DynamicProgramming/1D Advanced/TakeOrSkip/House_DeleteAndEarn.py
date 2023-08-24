"""
Spinoff of House Robber
    - Instead of houses, we have clusters of dupe numbers -> .sort()
    - Selecting one cluster means you are unable to take next cluster
    - " if num occurs multiple times in nums and we take one, we may as well take all of them"
"""
from collections import Counter
from functools import lru_cache
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """ what is max earnings considering index from 0 to i"""
        @lru_cache(None)
        def dp(i):
            print(i)
            # base
            if i < 0:
                return 0
            # recurse.. either take or skip this nums[i]
            num = nums[i]
            skip = dp(i - numCounts[num]) 
            take = dp(i - numCounts[num] - numCounts[num-1]) + num*numCounts[num]
            return max(skip, take)
        
        nums.sort()
    
        numCounts = Counter(nums)
        
        return dp(len(nums) - 1)
    
"""
Precompute: 
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def dp(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            # Apply recurrence relation
            # NOTE: if num is not one of nums... one of smaller subproblems will trickle up
            return max(dp(num - 1), dp(num - 2) + points[num])
        
        return dp(max_number)