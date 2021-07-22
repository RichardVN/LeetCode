class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # not 0, there must be 1 bit somewhere
        while n!= 0:
            res += 1
            # NOTE:  n AND n-1 flips least significant 1-bit to 0, keeps all other bits the same
            n = n & (n-1)
        return res

"""
For loop solution:
    - Mask of 1, compare and shift
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # mask of least significant bit
        mask = 1
        
        # 32 bits
        for i in range(32):
            # compare least significant bit
            if n & mask == 1:
                res += 1
            # shift bits right ("decimal goes left")
            n >>= 1
        return res