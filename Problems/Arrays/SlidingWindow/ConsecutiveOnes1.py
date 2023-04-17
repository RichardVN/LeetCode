"""
https://leetcode.com/problems/max-consecutive-ones/description/
Intuition:
    - Traverse and increment streak count if 1
    - if not 1, reset streak to 0

NOTE : easier than sliding window because we DONT shrink to find next i position. 
        We know immediately i is at j + 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        streak = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 0
        return max_streak

# with pointers
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                # j on valid 1
                streak = j - i + 1
                max_streak = max(max_streak, streak)
            else:
                # place i on valid window start
                i = j + 1
        return max_streak