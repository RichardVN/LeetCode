"""
https://leetcode.com/problems/rotate-array/description/

Key Takeaway: A subarray from back of array can be moved to the front, WITHOUT array needing to be sorted - 
        by using in-place reverses

Pseudo:
    - modulo k so that it is within N
    - make a reverse_subarray helper function
    - Move last k nodes to front using 3 reverses
        1. reverse entire array
        2. reverse first k elements in array
        3. reverse all other elements in array

Time: O(N) for reverses
Space: O(1) in place
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        # -- Move last k nodes to front using 3 reverses --
        # 1. Reverse Entire array
        nums.reverse()
        # 2. Reverse first K values, pass in first idx and last idx
        self.reverse_subarray(nums, 0, k-1)
        # 3. Reverse rest of list
        self.reverse_subarray(nums, k, N-1)

    def reverse_subarray(self, array, left, right):
        # NOTE: complement does NOT work if we are using subarray
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)

        # a shift N == k, would be no shift. Modulo to get k within size N
        k = k % N
        # initialize answer array
        res = [0] * N
        # each element is shifted LEFT N-k
        for i in range(N):
            res[i - (N-k)] = nums[i]
        nums[:] = res
