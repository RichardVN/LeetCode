"""
NOTES:
    we can use two sum I solution for O(N) space and time using hash table
    However, we can make use of the fact that is SORTED
        - any thing to left of ptr is GUARANTEED smaller
        - any thing to right of ptr is GUARANTEED bigger
        
    THERE IS EXACTLY ONE SOLUTION
    NO DUPE
    THIS IS 1-INDEXED
    
Approach:
- 2 pointer method while l < r
"""
# ex;  2  7  11  15         target = 9 
#      l         r
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0 
        r_ptr = len(numbers) - 1
        
        while l_ptr < r_ptr:
            total = numbers[l_ptr] + numbers[r_ptr]
            if total == target:
                return [l_ptr +1, r_ptr +1]  # NOTE: problem is 1 indexed
            elif total < target:    # too small, we need bigger sum
                l_ptr += 1
            else:                   # too big, we need smaller sum
                r_ptr -= 1
        # break loop, when l and r on top
        return None