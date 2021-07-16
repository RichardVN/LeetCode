"""
https://leetcode.com/problems/find-the-duplicate-number/

NOTE: we cannot use XOR to cancel indices and values. 
The number that is duplicated may be duplicated MANY times
"""

"""
Optimal Approach:  cycle detection

NOTE: 
    - 0 is not in nums, because there is another duplicated number
    - Each Value in nums can be a "node"
    - slow and fast both start at nums[0] node

Linked list: slow / fast are pointers to Node      Array: slow / fast are index positions

slow = slow.next                      -->          slow = nums[slow]
fast = fast.next.next                 -->          fast = nums[nums[fast]]

if we have [2,2,2,2], then it is just one node (2) that loops on top of itself
"""
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        # TODO: head "node" is first value, nums[0]
        slow = fast = nums[0]

        # we KNOW there is a cycle because there is a repeated number
        # NOTE: if there is a cycle, it takes at most O(N) to intersect
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            # when slow and fast are same idx, break
            if slow == fast:
                break
        
        print(slow, fast)
        # slow and fast are at X intersection, h steps away from entry
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

"""
Approach 2: Hash map
Space: O(N)
Time: O(N)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return None


"""
Approach 3: marking with negatives
    - NOTE: THIS CHANGES ORIGINAL ARRAY
    - values are limited to within index range, we can use marking

Time: O(N) to pass and mark
Space: O(1), but we modify original
"""
    
class Solution3: 
    def findDuplicate(self, nums) -> int:
        for i, num in enumerate(nums):
            idx_to_mark = abs(num) - 1
            # that index label has been seen
            if nums[idx_to_mark] < 0:
                return(abs(num))
            else:
                # mark that index label as seen
                nums[idx_to_mark] = - nums[idx_to_mark]
        print(nums)
        return -1