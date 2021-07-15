
""" 
Approach Bit Manipulation
- each number in list has a duplicate EXCEPT one

KEY NOTE:
- a XOR 0  = a
- a XOR a  = 0
- a XOR b XOR a   equivalent to   a XOR a XOR b

Time:  O(N)
Space:  O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # go thru each number and XOR to running XOR result
        # duplicates will transitively cancel, the single number will remain
        single = 0
                """ This is  single  =  num1 xor num2 xor num3 """

        for num in nums:
            single = single ^ num
        return single