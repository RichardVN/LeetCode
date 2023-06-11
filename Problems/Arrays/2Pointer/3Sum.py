"""
Intuition:
    - 3 sum adds additional dimension to 2 sum, so we can expect O(N^2)
    - Two Sum II finds two numbers that add to a target ... NOTE: must sort for TwoSumII
    - For each value in array, there must be Two Sum adding to - (value) so that there is
        a triplet summing to 0
            - NOTE: we want all triplets. we continue incrementing until l and r meet
            - NOTE: upon returning triplet, increment left until it is no longer same value
            
Algorithm:
    - Main: 
        - NOTE: SORT so we can two sum II
        - Iterate i through the array. Skip if same value as last index
        - perform two sum II on subarray [i+1 : to the end]
    - Helper: Finds 2 Sum for target - nums[i]
        - Create a Two SUM II helper function with two pointers. 
        - If we found a good pair, add the triplet to the result. 
        - Decrement RIght, Increment(s) left until new.


Time: O(N^2)      O(n log n) sort ... O(N) iterate array -> O(N) 2Sum
Space: O(log n)  or  O(N) timsort  for sorting.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # sort so we can use two sum II
        nums.sort()
        
        for i, num in enumerate(nums):
            # nums[i] is the first value in triplet. Increment if it is a dupe
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # use two sum for everything right of i
            left = i+1
            right = len(nums) - 1 
            target = - nums[i]              # (x+y) should cancel out z
            # keep moving pointers, and adding triplets to array
            while left < right:
                triplet_sum = nums[left] + nums[right] + num
                
                if triplet_sum < 0:
                    left += 1
                elif triplet_sum > 0:
                    right -= 1
                # TODO: Valid Triplet ->  1. Append Triplet , 2. increment left, 3. increment left if dupe value
                else:
                    result.append([nums[i],nums[left], nums[right]])
                    left += 1       # only need to change left,
                    # Avoid Dupes!  increment left until we get diff number
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return result
