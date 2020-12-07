# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# NOTE: Tip: When using a temp variable, consider a,b = b,a notation. Collapse statements to one line to avoid overwrite
    # python evaluates right hand expression and stores on stack, before assigning stuff on left hand
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
