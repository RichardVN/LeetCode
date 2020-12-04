
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        : type nums: List[int]
        : type target: int
        : returntype: List[int]
        """
        # value:index
        seen_values = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_values:
                # return the index of complement, stored in dict
                return [i, seen_values[complement]]
            else:
                seen_values[num] = i
        # no complements found
        return None
