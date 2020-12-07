# https://leetcode.com/problems/valid-mountain-array/submissions/
# TIPS:
# Get used to for loop over range, and while loop constructs
# when using i-1 or i+1 in a loop, make sure to adjust loop range
# first condition of while loop is always checked before second
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        # climb up
        # first condition breaks before trying to access out bounds
        while i+1 < N and arr[i+1] > arr[i]:
            i += 1                                  # make sure to have an increment to break out
        peak = i
        # peak can't be first or last element
        if peak == 0 or peak == N-1:                # while loop has two conditions. 1. Could have reached end
            return False
        # climb down
        for j in range(peak, N-1, 1):
            if arr[j+1] >= arr[j]:
                return False
        return True
