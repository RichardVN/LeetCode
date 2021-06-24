"""
Find Midpoint using number of elements / length of array
"""
print('-- Midpoint using number of items len(arr) -- ')

odd_array = [5, 6, 7]
mid_idx = len(odd_array)//2
print('Odd Array mid', odd_array[mid_idx])

even_array = [5, 6, 7, 8]
mid_idx_left = len(even_array)//2 - 1
mid_idx_right = len(even_array)//2
print('Even array left mid', even_array[mid_idx_left])
print('Even array right mid', even_array[mid_idx_right])

"""
Find Midpoint using first index and last index
NOTE: if low is just 0 index,  then   mid = len(arr)-1 // 2
"""
print('-- Midpoint using lowest, highest indices -- ')

odd_array = [5, 6, 7]
low = 0
high = 2
mid_idx = low + (high-low)//2
print('Odd array mid',odd_array[mid_idx])


even_array = [5, 6, 7, 8]
low = 0
high = 3
mid_idx_left = low + (high-low)//2
mid_idx_right = low + (high-low)//2 + 1
print('Even array left mid', even_array[mid_idx_left])
print('Even array right mid', even_array[mid_idx_right])


"""
Find midpoint of linked list
NOTE: in even node list, this retrieves the right mid point
"""
# slow = head
# fast = head

# while fast and fast.next:
#     fast = fast.next.next
#     slow = slow.next

# mid_node = slow