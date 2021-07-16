'''
each integer appears once or twice
    indices: 0 to n-1
    values:  1 to n  (ALL POSITIVE)
We can do O(1) space if we use marking
NOTE: we use abs to make sure we append the original positive values to res
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for idx, num in enumerate(nums):
            mark = abs(num) - 1
            # already seen, add ABSOLUTE original value to res
            if nums[mark] < 0:
                res.append(abs(num))
            # not seen yet, mark
            else:
                nums[mark] = - nums[mark]
        return res