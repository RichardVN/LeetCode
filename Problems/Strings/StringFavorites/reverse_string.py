"""
NOTE: in even num array, we have to make sure to swap mid (left middle) with right middle
Pythonic solution using complements
Intuition:
    - We swap an element with its complement until after middle idx
Steps:
    1. find middle index
    2. Loop until middle idx (inclusive)
        a. swap element at i with element at ~i using  python var swap
Ti
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


"""
Traditional 2 pointers
Intuition:
    - pointer at each end
    - swap values at pointers and walk pointers in
    - Not necessary to swap if pointers same spot (this means only a single middle)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        # note if left ever equal right, that means we have odd num N, with single middle
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
