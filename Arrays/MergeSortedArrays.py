# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # initialize ptrs to indices (last value)
        i = m - 1
        j = n - 1
        k = (m+n) - 1

        # we run out of nums of list when index reaches -1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # if we run out of nums2, nums1 is already sorted
        # if we run out of nums1, place rest of nums2 into nums1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]

        # Alternate Solution" using sort
        # complexity (m+n) log (m+n)
        # sorted uses aux space O(N)
        # nums1[:] = sorted(nums1[0:len(nums1)-len(nums2)] + nums2)
