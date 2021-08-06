import heapq 

a = [5,3,6,9,4]

# Does NOT have a return value. Modifies List.
heapq.heapify(a) 
print(a)

# push element to heap  O(log n)
heapq.heappush(a, 0)
# Removes min element   O(log n)
heapq.heappop(a)
# peak minimum element  O(1)
top = a[0]

# merge two sorted iterables into a single sorted output
b = [1,3,4]
c = [0,3,8]
merged_iterator = heapq.merge(b , c)
for item in merged_iterator:
    print(item)

# get n largest from heap
n_largest_list = heapq.nlargest(3 , a)
print(n_largest_list)