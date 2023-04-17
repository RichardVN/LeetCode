"""
Why Sliding Window?:
- Contiguous subarray
- OPTIMIZE:  maximize consecutive 1's
- CONSTRAINT for validity:  flipped_zeroes <= 3

Pseudo:
- for loop traversal with j
    - update constraint based on j new position
    - if invalid, shrink window until valid
    - update optimization with now valid window

    # Same as consecutive ones II

"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        flipped = 0
        longest = 0 
        for j in range(len(nums)):
            # update constraint
            if nums[j] == 0:
                flipped += 1
            # shrink Invalid until valid
            while flipped > k:
                i += 1
                if nums[i-1] == 0:
                    flipped -= 1
            # valid
            longest = max(longest, j-i +1)
        return longest
