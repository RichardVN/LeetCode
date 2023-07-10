"""
Keys to Question:
- stack of indices that are pending nextGreater value
    - only find nextGreater of nums2 if it is also in nums1  -> HASH MAP
- determine nextGreater from nums2 array,  but store the result with relation to nums1 index

"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # list of integers ... nextGreaters[i]  contains  number that is nextGreater of nums1[i]
        nextGreaters = [-1] * len(nums1)

        valToIndex = { val : i for i, val in enumerate(nums1) }

        # stack of nums2 indices ... we are pending finding the next greater val for nums2[i]
        s = []

        for nums2i, nums2val in enumerate(nums2):
            # we have FOUND the next greater for stack top
            while s and nums2val > nums2[s[-1]]:
                # pop and update result array
                #  popppedIdx → poppedVal → nums1Idx == resultIdx
                poppedIdx = s.pop()
                poppedVal = nums2[poppedIdx]

                resIdx = valToIndex[poppedVal]
                nextGreaters[resIdx] = nums2val

            # push nums2i if its value is also in nums1
            if nums2val in valToIndex.keys():
                s.append(nums2i)

        return nextGreaters