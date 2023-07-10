"""
Use monotonic decreasing stack
- push items that are pending next Greater element

TODO: we need to search circularly, so we just pass the elements in the stack twice
    - double for loop so that we can use remainding pending elements from 1st iteration
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextGreaters = [-1] * len(nums)
        s = []

        for _ in range(2):
            for i, num in enumerate(nums):
                # found next greater for stackTop's num
                while s and num > s[-1][1]:
                    poppedIdx, poppedNum = s.pop()
                    # update result array
                    nextGreaters[poppedIdx] = num
                # need to find next greater for these vals
                s.append( (i, num) )

        return nextGreaters