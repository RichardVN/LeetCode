"""
Intuition:
- at each number, the product of all except self is (product left) * (product right)
- we can make two passes
    - one pass to find product to left  ,  left -> right
    - one pass to find product to right  , right -> left

Time:O(N), multiple linear passes to build product_left and product_right arrays
Space: O(2N), space to hold products_left and Product_right

NOTE: for O(1) space, just build product_left into result array
        - then, iterate reverse, with a variable to hold product_right
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        
        product_left = [0] * len(nums)
        product_left[0] = 1
        for i  in range(1, len(nums)):
            product_left[i] = product_left[i-1] * nums[i-1]

        product_right = [0] * len(nums)
        product_right[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            product_right[i] = product_right[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            answer[i] = product_left[i] * product_right[i]
            
        return answer