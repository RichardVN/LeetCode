"""
Intuition:
    - we have limited range of numbers, all positive
    - we can mark indices of found numbers
    - loop thru range, find the values that are positive (aka corresponding number not seen)
    - NOTE: make sure to use abs so we dont mark NEGATIVE index
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        # if we see 1, mark 1st index aka. 0
        for idx, num in enumerate(nums):
            #NOTE: we might have marked a number negative AHEAD of i ptr
            idx_to_mark = abs(num) - 1
            # use abs in case we already marked this
            nums[idx_to_mark] = - abs(nums[idx_to_mark])
            
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0 :
                res.append(i)
        print(nums)
        return res