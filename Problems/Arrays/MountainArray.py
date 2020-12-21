# https://leetcode.com/problems/valid-mountain-array/submissions/
"""
NOTE: 
    - if we access value at i+1, then i+1 has to be less than size N
    - In multiple while conditions. The fist condition is checked
    and can break the loop before accessing the second condition

Intuition:
    1. Climb "Up" the array. While loop iterates while a) indices within bounds and b) increasing slope
    2. If slope no longer increasing, assign value to Peak index
    3. Check if peak is valid (not one of the ends)
        a.) if peak is invalid return False
    4. Iterate from peak to end of array
        a.) if slope does NOT decrease return False
    5. Return true

Time: O(N), Iterate from 0 to peak, then peak to N-1
Space: O(1)
"""
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
