"""
Intuition:
- we want to check if we have seen something before, O(1) access using HASH MAP
- we create a set from list, which remove duplicates
    - if duplicates: set length differs from array length
    

"""

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use a set, if there are any duplicates then set length will be different
        seen = set(nums)
        # return true if value appears twice, aka return true if length differs
        return len(seen) != len(nums)

"""
Solution 2:  sort first
Time: O(n log n),  space:O(1)
- sort
- iterate thru array, duplicates will be next to each other

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False