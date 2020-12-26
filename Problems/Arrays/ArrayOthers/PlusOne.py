"""
NOTE: 
    - positive digits, less than 10
    - similar to linked list add, with carry

Intuition:
    - Loop starting from least significant digit
    - if the first index, add one
    - Two cases:
        - sum < 10:
            then the value at that index is digit_sum and we return (don't set carry to 0 because we return anyways)
        - sum >= 10:
            then the value at that index is 0, and we set carry to 1
    - after all addition, if we still have carry: append 1 to beginning
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        N = len(digits)

        for i in range(N-1, -1, -1):
            digit_sum = digits[i] + carry
            # initial plus one
            if i == N-1:
                digit_sum += 1
            # there is no carry
            if digit_sum < 10:
                digits[i] = digit_sum
                return digits
            # there is a carry
            else:
                digits[i] = 0
                carry = 1
        # we have reached beginning but still have carry to appendleft
        if carry == 1:
            digits.insert(0, 1)
        return digits
