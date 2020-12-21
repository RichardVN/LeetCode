# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""
NOTE: 
Whenever we need temp, consider a,b = b,a variable swap. 
Collapse statements to one line to avoid overwrite before assignment
    # python evaluates right hand expression and stores on stack, before assigning stuff on left hand

Intuition:
Iterate right to left, so at each element, we know what biggest to right is.
Have a variable to store biggest seen so far, initialize with right most element.

Time: O(N)
Space: O(1)
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        # initially, biggest is last element
        biggest = arr[-1]
        # loop right to left, so we know what "biggest to right" is. Dont start at last element
        for i in range(N-2, -1, -1):
            # save original value at i
            temp = arr[i]
            # replace value with biggest seen so far (to right of i)
            arr[i] = biggest
            # update biggest if value at i is bigger
            biggest = max(temp, biggest)

            #NOTE: Pythonic alternative. Collapse statements to single line to avoid overwrite. Right side evaluated first, on stack.
            # arr[i] = biggest
            # biggest = max(arr[i], biggest)
                # --> arr[i], biggest = biggest, max(arr[i], biggest)

        arr[-1] = -1

        return arr
