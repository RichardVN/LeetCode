"""
Similar to max sum subarray (kadane's)

Keep running vals of minimumProduct and maximumProduct.
    - if the next val is negative, min will become max
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            # we have to save curMax for calculation of curMin
            newMax = max(num, num * curMax, num * curMin)
            # next value could be negative, which would mean curMin would be used for max
            curMin = min(num, num * curMax, num * curMin)

            curMax = newMax
            res = max(res, curMax)
        return res
