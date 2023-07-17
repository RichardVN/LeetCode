"""
The issue with DUPLICATES is that taking the first 2 is seen as different than taking the second 2
-> ALLOWED: [2], [2,2*]
-> SEEN AS SAME:  [1,2] and [2,1] ... [2, 2*] and [2*, 2]

TODO: we can ensure duplicates are next to each other by sorting
By nature of decision tree (take / not take):
    - we have subtrees that must contain one 2, two 2's ... etc
    - after we pop() we are DONE with that 2 value

Time: O(N * 2^N)  ... there are 2^N subsets (2 decision branches, N decisions)  and  takes N to copy each subset to answer
Space: O(N) to maintain current subset while backtracking
"""

class Solution:
    def subsetsWithDup(self, nums):
        def dfs(i):
            # made decision for each nums[i]
            if not i < len(nums):
                subsets.append(subset[:])
                return
            # Decision tree
            subset.append(nums[i])
            dfs(i+1)        # this will TAKE until base case.
            subset.pop()    # we are at last valid i. pop last element.
            # we are DONE with Taking any number of popped_num. Increment i to new num
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        #TODO : sort so dupes are adjacent
        nums.sort()
        subset, subsets = [], []
        dfs(0)
        return subsets
    
"""
Alternative using For Loops
- Subsets -> we always append
- for loop handles index bounds
"""
class Solution2:
    def subsetsWithDup(nums):
        def dfs(i):
            # append this subset before decision
            subsets.append(subset[:])

            for j in range(i, len(nums)):
                # we just popped , dont want to use same num
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                dfs(j+1)
                # subset.pop()

        nums.sort()
        subset, subsets = [],[]
        dfs(0)
        return subsets

c2 = Solution2
res = c2.subsetsWithDup(nums=[1,2,3])
print(res)