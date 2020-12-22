# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
NOTE: 
    - Original Array is SORTED, make use of this!
    - Key thing to notice is that the values from left decrease until 0, and then values to right increase from 0
    the further from zero, the higher the square

"""
"""
SOLUTION 1 - use deque to append values to left in O(1). So we append biggest, and then smaller values to left of that.
from collections import deque
Intuition:
    - We know that the biggest values are at the ENDS --> we can convert to a deque and access ends in O(1)
    - Two pointer method
        NOTE: We use <= comparison, to ensure that ALL values are added
        - Take vals at the ends, and compare
        - append the bigger value to the answer list

Time: O(n), no nested loops.
Space: O(n), we have to make an array to hold answer, size of N
"""
class Solution:
    def sortedSquares(self, nums):
        answer = []
        left = 0
        right = len(nums) - 1
        while left <= right:                            # left == right if both are at value 0
            if abs(nums[left]) >= abs(nums[right]):
                answer.append(nums[left]*nums[left])
                left += 1
            else:
                answer.append(nums[right]*nums[right])
                right -= 1
        # now we have answer list in decreasing order. We can in-place reverse in O(N) time
        answer.reverse()
        return answer


solution = Solution()
test_arr = [-5, -3, -1, 0, 2, 8]
squares = solution.sortedSquares(test_arr)
print(squares)



"""
SOLUTION Alternate - use in place sort
Time: O(nlogn) due to sort
Space: O(1), overwrite in place, sort in place
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = num**2
            nums.sort()
            return nums



