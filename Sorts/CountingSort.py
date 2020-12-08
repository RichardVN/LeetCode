"""
Use This when the range of possible values (K) is equal to or less than the number of elements in array (N)
Time Complexity: O(2n + 2k), O(n+k) ... O(n) if k is small enough
Space Complexity: O(k) in count and placement arrays

# NOTE: we fill same numbers R -> L, making this STABLE: Order of same nums preserved
# NOTE: the values of original array must be POSITIVE, or else we have negative index access for array, ex. arr[-2]

"""

def count_sort(arr, max_value):
    
    # 1. Initialize the count array, which counts the occurences of each value in range k. O(k)
    count = [0 for i in range(max_value+1)]   # + 1 because inclusive 0 and max value. NOTE: always starts from 0 index

    # 2. map the counts of each value into count array.  O(N)
    # NOTE: This is like a hash map freq chart where the VALUE of orig array is the KEY of this map. We use array so its ordered.
    for num in arr:
        count[num] += 1
    print(count)

    # 3. Transform count array into running count. From second element to end.   O(k-1)
    for i in range(1, len(count)):
        count[i] += count[i-1]
    # Count now holds the LAST POSSIBLE INDEX, at which that value can be found

    # 4. Initialize sorted_array using length of original array   O(N)
    sorted_array = [0] * len(arr)

    # 5. Place elements from original array into proper place at sorted_array, using indices from count array
    for num in arr:
        placement_idx = count[num] - 1              # NOTE: -1 because we use indexing at 0
        sorted_array[placement_idx] = num           # insert the number into its proper position in sorted array
        count[num] -= 1                             # NOTE: The last idx at num decreases by one, for duplicate vals. 
    return sorted_array


# Test
test_array = [1,9,2,10, 4]
sorted_result = count_sort(test_array, max_value=10)
print(f"Original:{test_array} Sorted: {sorted_result}")
