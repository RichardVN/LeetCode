"""
NOTE: on second pass, make sure biggest isn't being compared with biggest (itself)
    continue to next loop
Intuition:
    - we are guaranteed one biggest number
    - 1. First pass: find biggest number and its index
    - 2. Second pass: compare every other value, except itself, and return
            -1 if biggest < 2*num
    - 3. Return the biggest_idx
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        biggest = -float("inf")
        biggest_idx = -1
        for i, num in enumerate(nums):
            if num > biggest:
                biggest = num
                biggest_idx = i
        for i, num in enumerate(nums):
            if i == biggest_idx:
                continue
            if biggest < 2*num:
                return -1
        return biggest_idx
