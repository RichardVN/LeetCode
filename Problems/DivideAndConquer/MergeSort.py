from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Given nums array, return SORTED nums array """
        def mergeSort(nums):
            # Base Case: we have reached the SMALLEST size. Trivial case to sort
            if len(nums) <=1:
                return nums
            m = len(nums) // 2
            # 1. Recursively Call smaller subproblems... until base case is reached
            # unlike dp which is typically (i-1) ... here we call function on HALF input size
            sortedleft = mergeSort(nums[:m])
            sortedright = mergeSort(nums[m:])
            
            # 2. Use answer to subproblems to solve this problem
            # "Using sorted left and right, how do we return sorted total?"
            return merge(sortedleft, sortedright)
        
        def merge(l1, l2):
            res = []
            i1 = i2 = 0

            while i1 < len(l1) and i2 < len(l2):
                if l1[i1] <= l2[i2]:
                    res.append(l1[i1])
                    i1 += 1
                else:
                    res.append(l2[i2])
                    i2 += 1

            # one of these lists will be empty        
            res.extend(l1[i1:])
            res.extend(l2[i2:])

            return res

        return mergeSort(nums)




