# Same as consecutive ones II
# use for loop instead of while loop
    # NOTE: key difference is that the iterator in for loop only makes it to last index N-1, and never becomes N
            # In a while loop, iterator becomes N, the value that breaks the condition
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        j = 0
        i = 0

        # i will end on the final index of list
        for i in range(len(A)):
            if A[i] == 0:
                zeroes += 1

            # expand window without shifting start
            if zeroes <= K:
                continue
            # invalid window, must shift start until zeroes valid again
            else:
                j += 1
                # if we 'removed' a zero
                if A[j - 1] == 0:
                    zeroes -= 1
        print(len(A), i, j)
        return i-j + 1
