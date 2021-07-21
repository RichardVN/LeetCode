"""
Approach: sort, TwoSumII , update answer triplet_sum IF triplet_dif is lowest magnitude
    NOTE: use absolute value of difference to see how far away from target
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_dif = float("inf")
        closest_sum = 0
        for idx, num in enumerate(nums):
            # update TwoSum II parameters
            two_sum_target = target - num
            left = idx + 1
            right = len(nums) - 1
            
            while left < right:
                triplet_sum = nums[left] + nums[right] + num
                triplet_dif = abs(target - triplet_sum)
                
                if triplet_dif < closest_dif:
                    print(num, nums[left], nums[right])
                    closest_dif = triplet_dif
                    closest_sum = triplet_sum
                
                if triplet_sum < target:
                    left += 1
                elif triplet_sum > target:
                    right -= 1
                else:# match exactly
                    return target
        return closest_sum
                    