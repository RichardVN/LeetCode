"""
Approach 3: Gauss's law
Intution:
    - Compare sum of nums to sum if no nums were missing
    - NOTE: summing a range of number is O(N), O(1) operation
"""
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sum_none_missing = sum(range(N+1))
        sum_list = sum(nums)
        missing = sum_none_missing - sum_list
        
        return missing

"""
Approach 1: Hash map
NOTE: "Contain query"

Time: O(N)
Space:  O(N) for hash map

"""

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        # INCLUSIVE
        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i
        return None

"""
Approach 2:  sorting

Time: O(n log n)
Space: O(1)

NOTE: consider edge case where the missing number is the last number
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
        