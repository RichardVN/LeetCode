"""
NOTE: no need to pass in index,  we are allowed to choose nums from prior indices
dfs()
BaseAppend Case:  when we hit length of original nums
Recursive Decision Case:  for loop through all nums, and take the num if it is not already in perm

TIME:  O(N! * N)  ,    N! permutations and permutation_size is N
SPACE: O(N)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we DONT pass in i, because we cannot "exhaust" a candidate
        # only condition is that candidate is not already in permutation
        def backtrack():
            # base case: append when reach length of nums
            if len(perm) == len(nums):
                perms.append(perm[:])
                return

            # look through all nums options
            for num in nums:    
                if num not in perm: 
                    # Append num that's not already in curr
                    perm.append(num)
                    backtrack()
                    perm.pop()
            
        perm = []
        perms = []
        backtrack()
        return perms

