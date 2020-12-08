# https://leetcode.com/problems/squares-of-a-sorted-array/
# Time: O(nlogn) due to sort
# Space: O(1), overwrite in place, sort in place
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square and overwrite in place
        for i, num in enumerate(nums):
            nums[i] = num**2
        nums.sort()
        return nums
# NOTE: this overwrites the original input array.

# NOTE: Two pointer method. 
# No sorting, make use of the fact that the given array is sorted
# after squaring, we strictly decrease towards middle, strictly increase from middle
# Time: 
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return return_array
