"""
Intuition:
- Similar to pivot index
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
        N = len(nums)
        res = [1]*N
        # array of product to left
        product_left = 1
        for i in range(len(nums)):
            res[i] = product_left       #TODO:  assign product_left at i BEFORE multiplying by num at i
            product_left *= nums[i]
        print(res)
        # now we get product_right and multiply with whatever is at i
        product_right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * product_right
            product_right *= nums[i]
        
        return res