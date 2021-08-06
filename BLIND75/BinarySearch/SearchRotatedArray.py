"""
Approach: find if mid and target in left or right partition. Binary search
    Time : O(log n)
    Space: O(1)

Notice After rotation:
    - Bigger numbers on left partition, smaller numbers on right partition

Intuition:
    - find middle idx
    - if [mid] == target: return mid
    - Left Sorted portion:  If [mid] >= [Left]
        - Check right half if target > [mid]  OR  target not in left sorted
        - else check to left of mid
    - else Right Sorted Portion
        - check left half if target < [mid] OR target not in right sorted
        - else check to right of mid
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        
        while l <= r:
            mid = l + ((r-l) // 2)
            
            # found mid
            if nums[mid] == target: 
                return mid
            
            # adjust mid depending where mid and target is
            
            # mid is in left sorted portion. It is possible middle and left are same value
            if nums[mid] >= nums[l]:
                # check to right of mid
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
            # else right portion
            else:
                # check left of mid
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1