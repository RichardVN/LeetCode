# https://leetcode.com/problems/check-if-n-and-its-double-exist/

"""
NOTE: Care for case in which the 2N double is after N. For each value, we want to check if we have seen its half.
    - In two sum, we only had one other value (complement) that would make function return true
    - in this problem, we have TWO possible values - n*2 and n//2 that could make the function return true

Intuition:
    - Put seen values in a set
    - One Pass: A double occurs if
        1. There is a value that is 2 * num in seen set
        2. There is a value that is num // 2 in seen set (if num is even)
        
    NOTE: if we do two passes, we don't need condition two. The double has to already be in the set. 
        -> But we have to be careful for the case ONLY ONE zero

Time: O(N) one pass 
Space: O(N) to make a set
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        seen = set()
        for num in arr:
            double = num * 2
            # check if a number's double has been seen before
            # remember the num can be another num's double
            half = num // 2 if num % 2 == 0 else None
            if double in seen or half in seen:
                return True
            else:
                seen.add(num)
        return False
