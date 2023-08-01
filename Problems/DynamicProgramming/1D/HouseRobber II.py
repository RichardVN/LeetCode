class Solution:
    def rob(self, nums: List[int]) -> int:
        # trivial subproblems
        if len(nums) <= 2:
            return max(nums)

        prev1, prev2 = 0, 0

        # first house up to but not including last house
        # If we take from first house, we CANT take from last house
        for i in range(len(nums) - 1):
            curr = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        pass1 = curr
        
        prev1, prev2 = 0, 0
        # second house 1 up to AND INCLUDING last house
        # if we take from last house, we CANT take from first house
        for i in range(1, len(nums)):
            curr = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        pass2 = curr

        return max(pass1, pass2)