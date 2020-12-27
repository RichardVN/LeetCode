# https://leetcode.com/problems/height-checker/
"""
NOTE: The range of inputs is limited, POSITIVE integers. The range K = 100 < N elements in array. => COUNT SORT

Intuition:
    - sort the array
    - Compare the sorted_array to original array

Count Sort:
    - Time: O(N) using count sort
    - Space: O(N) using count sort
Inbuilt Sort:
    - Time: O(N log N) using .sort()
    - Space: O(1) using in place sort

"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Time: O(n log n) sorting. O(n) if using count_sort
        # Space: O(N) new list

        def count_sort(arr, max_value):
            # 1. Initialize the count array, which counts the occurences of each value in range k. O(k)
            # + 1 to account for 0 index.
            count = [0 for i in range(max_value + 1)]

            # 2. map the counts of each value into count array.  O(N)
            for num in arr:
                count[num] += 1

            # 3. Transform count array into running count. From second element to end.   O(k-1)
            for i in range(1, len(count)):
                count[i] += count[i-1]

            # 4. Initialize sorted_array using length of original array   O(N)
            sorted_array = [0] * len(arr)

            # 5. Place nums into sorted_arr and decrement count 
            for num in arr:
                placement_idx = count[num] - 1
                sorted_array[placement_idx] = num
                count[num] -= 1
            return sorted_array

        # sort array with count_sort because range of values is <= N elements
        sorted_heights = count_sort(heights, 100)
        # compare changes from original array to sorted array
        changes = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                changes += 1
        return changes
