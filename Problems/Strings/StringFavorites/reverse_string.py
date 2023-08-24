
"""
Iterative Solution:  2 pointer swaps
Intuition:
- IN PLACE modification, think of 2 pointers swapping
- walk inwards with 2 pointers, swap values
"""
class Solution:
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

"""
Recursive Solution: 2 pointer swaps. TODO: While loop w/ iterattion is replaced with recursion w/ updated index states

Instead of using while loop, we use recursive calls with iterated pointers
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def dfsRev(l, r):
            # Base
            if l >= r:
                return
            # recursive ... swap left and right and recursive call middle
            s[l], s[r] = s[r], s[l]
            dfsRev(l + 1, r - 1)
        
        l = 0
        r = len(s)-1
        dfsRev(l, r)


"""
https://leetcode.com/problems/reverse-string/description/
NOTE: in even num array, we have to make sure to swap mid (left middle) with right middle
Pythonic solution using complements
Intuition:
    - We swap an element with its complement until after middle idx
Steps:
    1. find middle index
    2. Loop until middle idx (inclusive)
        a. swap element at i with element at ~i using  python var swap

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid_idx = (len(s) - 1) // 2
        # swap char with complement until we reach mid.
        # For even N, mid is LEFT middle , and we have to include in swap. Single mid swaps itself.
        for i in range(mid_idx + 1):
            s[i], s[~i] = s[~i], s[i]