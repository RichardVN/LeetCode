"""
Similar to two-sum but we can do in constant space

Intuition:
- have two pointers at front and back
- Sum the values at two pointers.
    Case 1: sum is the target: return the indices (the pointers)
    Case 2: sum is too high: -> we decrease the right pointer to decrease sum
    Case 3: sum is too low:  -> we increase the left pointer to increase sum
    NOTE: this only works because the list is sorted and we can guarantee
    that higher indices have higher values and lower indices have lower values

Time: O(N)
Space: O(1), no hash map needed. We do not need to know what we have seen before, because the
        "good pair" indices are towards the middle if they exist
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            lr_sum = numbers[left] + numbers[right]
            if lr_sum == target:
                print(left, right)
                return [left, right]
            elif lr_sum > target:
                right -= 1
            else:
                left += 1
        return -1
