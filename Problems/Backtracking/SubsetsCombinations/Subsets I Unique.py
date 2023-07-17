"""
Find all valid subsets of nums[] where each num is UNIQUE
    - Num subsets is equivalent to total nCk combinations for all k values
    - Decision Tree has 2 branches:  take or not take

Time: O(N * 2^N)  ... there are 2^N subsets (2 decision branches, N decisions)  and  takes N to copy each subset to answer
Space: O(N) to maintain current subset while backtracking
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # context subsets and nums
        # dfs helper .. appends subset to substet   ``
        def dfs(i):
            # base:  we have made Take decision for every i
            if i >= len(nums):
                subsets.append(subset.copy()) # TODO: need to append a COPY... subset is continually mutated
                return
            subset.append(nums[i])  # TAKE item decision
            dfs(i+1)        # This will dfs incrementing i until base case. 
            subset.pop()    # This line first executes on last valid i. 
            dfs(i+1)        # find valid subsets given this backtrack
        
        subsets = []
        subset = []
        # start decision tree at index 0
        dfs(0)
        return subsets


"""
Using for loop instead of base case
"""
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            # append subset before making a decision
            subsets.append(subset[:])

            # base : Remaining values we need to decide INCLUDE or EXCLUDE
            for j in range(i,len(nums)):
                # decision
                subset.append(nums[j])
                # Decision made. Make decisions starting at next index
                dfs(j+1)
                # backtrack decision
                subset.pop()

        subsets = []
        subset = []
        dfs(0)
        return subsets
