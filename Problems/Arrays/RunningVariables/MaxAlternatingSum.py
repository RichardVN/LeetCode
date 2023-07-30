"""
Memo Cache:
- Keys: (i, EVEN/ODD)
- Value: max sum

Decision Tree
- Take item (either add if even or subtract if odd)
- Skip item
"""
class Solution:
    def maxAlternatingSum(self, nums):
        def dfs(i, parity):
            if (i, parity) in memo:
                return memo[(i, parity)]
            if i >= len(nums):
                return 0
            # recursive case... "skip" this num and take last EVEN, or add to last ODD
            if parity == EVEN:
                memo[(i, parity)] = max( dfs(i+1, EVEN) ,  nums[i] + dfs(i+1, ODD))
            else:
                memo[(i, parity)] = max( dfs(i+1, ODD) ,  (-1)*nums[i] + dfs(i+1, EVEN))
            return memo[(i, parity)]

        
        EVEN = 0
        ODD = 1
        memo = {}
        return dfs(0, EVEN)
    
"""
Iterative with few variables
"""
class Solution:
    def maxAlternatingSum(self, nums):
        odd = even = 0
        for num in nums:
            # assign in one-line, to prevent overwrite of prev values
            odd, even = max(odd, even - num), max(even, odd + num)
        return even