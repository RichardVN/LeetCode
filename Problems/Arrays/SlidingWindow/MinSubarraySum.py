"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
Why Window?
- continguous subarray
- constraint: sum >= target
- minimize the size of subarray

Window method
- expand out with r, until we meet constraint
- while valid, shrink with l
    - update best answer
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_size = float(inf)
        l = 0
        window_sum = 0

        # expand out 
        for r, num in enumerate(nums):
            window_sum += num

            # while valid, greedily shrink
            while window_sum >= target:
                # update valid answer before shift
                minimum_size = min(minimum_size, r - l + 1)
                # shift left marker
                window_sum -= nums[l]
                l += 1

        return 0 if minimum_size == float(inf) else minimum_size