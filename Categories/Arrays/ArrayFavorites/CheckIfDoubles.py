# https: // leetcode.com/problems/check-if-n-and-its-double-exist/

# NOTE: Care for case in which the 2N double is after N. For each value, we want to check if we have seen its half.
# In two sum, we only had one other value (complement) that would make function return true
# in this problem, we have TWO possible values - n*2 and n//2 that could make the function return true

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        seen_values = set()
        for num in arr:
            double = num * 2
            # check if a number's double has been seen before
            # remember the num can be another num's double
            half = num // 2 if num % 2 == 0 else None
            if double in seen_values or half in seen_values:
                return True
            else:
                seen_values.add(num)
        return False
