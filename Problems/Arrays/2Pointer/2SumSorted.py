"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Similar to two-sum but we can do in constant space
NOTE: there is one exact solution, if multiple then we continue incrementing L and R

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
        l = 0
        r = len(numbers) - 1

        while l < r: 
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1] # NOTE: for this specific problem, they want 1-indexed array
            elif total < target:
                l+=1
            else:
                r-=1
        return None