"""
DP:  start from smallest subproblem, LIS at last char in string

Procedure:
    - LIS[] size of len nums
    - Iterate i backwards
        - iterate j thru elements right of i
            - if value increases from i to j
                - compare max of LIS[i] to LIS[j] + 1

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP array for each index of input array
        LIS = [1] * len(nums)
        
        # go reverse order
        for i in range(len(nums)-1, -1, -1):
            # go thru every sub sequence AFTER i
            for j in range(i, len(nums)):
                # TODO: does value INCREASE from i to j, then we can dp compare to j
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                
        # return max increasing sub sequence starting from any index
        return max(LIS)