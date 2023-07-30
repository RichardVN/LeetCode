class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        runningSum = 0
        for num in nums:
            runningSum += num
            res = max(res,runningSum)

            # if we made subarray negative, we reset
            if runningSum < 0:
                runningSum = 0
                
        return res

#  Sliding window approach.
#  NOT necessary because everytime we move L, we do a FULL reset by jumping l to r and resetting sum.
#  we never use L to incrementally shrink window and constraint.
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = nums[0]

        currSum = 0
        for r in range(len(nums)):
            # before adding R .. decide if the prior currSum (prefix) is worth keeping. If negative, discard and reset
            if currSum < 0:
                # TODO: since we fully reset by jumping l to r and never use l, we can just use running variables instead
                l = r
                currSum = 0
            currSum += nums[r]
            res = max(res,currSum)

        return res