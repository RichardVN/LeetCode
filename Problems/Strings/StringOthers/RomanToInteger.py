"""
Approach: Hash map Roman to integer value, left -> Right, check if double-Roman first
NOTE: it is impossible to hit one of the double-letter strings, just by using single-letter values

pointer i iterate thru Roman string
- check if double char string  s[i:i+2] is in map, increment by two  (exclusive right boundary)
- use single char string and increment by 1

Time: O(1) , integer value limited
Space: O(1) Constant

"""

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case. If i is at idx BEFORE last digit in s
            if i < len(s) - 1 and s[i:i+2] in values:
                total += values[s[i:i+2]] 
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total