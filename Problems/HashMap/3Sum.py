
"""
The key is to SORT

- UNLIKE two sum, there are multiple solutions, not just exactly one
- we have to eliminate duplicates by moving left marker

approach:
- SORT array so we can use two sum
- loop through array
- if value of i is same as left, we skip
- for each index i, we look at the other elements for a two sum that adds to - arr[i]
    - we keep checking for ALL two sums, that are not duplicates
    - each time we find a triplet, while loop to move left marker
- return results

Time: O(N logN) sort, O(N) to step through array, O(N) to use two sum,  Total O(N^2)
Space: we sort so, O(N)

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # sort so we can use two sum II
        nums.sort()
        
        for i, num in enumerate(nums):
            # Continue if outer loop i is duplicate. We use IF statement b/c for loop not while
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # use two sum for everything right of i
            left = i+1
            right = len(nums) - 1 
            
            # keep moving pointers, and adding triplets to array
            while left < right:
                total = nums[left] + nums[right]
                if total < - nums[i]:
                    left += 1
                elif total > -nums[i]:
                    right -= 1
                # we found match
                else:
                    result.append([nums[i],nums[left], nums[right]])
                    left += 1       # only need to change left,
                    right -= 1
                    #avoid duplicates!
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return result
            
            