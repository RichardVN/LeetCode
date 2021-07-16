"""
NOTE: WHY BIT??
    1. looking for a single number
    2. Values are limited to range of indices, so we can match and cancel

Approach 1: Bit Manipulation. XOR n with every index and value

Notice that:
- range of distinct numbers is [0, n]
- indices of array is [0, n)
- a XOR a is just 0 (cancels out)
- if we had NO missing number, we XOR indices and range 0 thru N and we should get 0
    - there is one missing number that is not cancelled out, we are left with it
NOTE: initializing missing as n
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        missing = N
        """ XOR every index and value in nums, and XOR n"""
        for idx, num in enumerate(nums):
            missing = missing ^ idx ^ num
        return missing

"""
Approach 2: Compare sum of None_missing to sum of Missing

"""
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sum_none_missing = sum(range(N+1))
        sum_list = sum(nums)
        missing = sum_none_missing - sum_list
        
        return missing
    

"""
Approach 3: Hash map
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
Approach 4:  sorting

Time: O(n log n)
Space: O(1)

NOTE: consider edge case where the missing number is the last number
"""
class Solution2:
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
    
