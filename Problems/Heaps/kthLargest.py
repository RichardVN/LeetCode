"""
TODO: 
Key: we don't need original values, pop all the the mins until we have k largest values

Pseudo:
    1. INIT:  
        - heapify the array in O(N) time.  Remove mins until we have k largest

    2. ADD:
        - heappush val to heap O(log K)
        - Check if we exceed k values:  => heappop()
        - the "kth largest" is actually smallest value, so return minheap[0]

// Heap Method Complexities //
Heapify:  O(N)
Heap push/remove:  O(log K)
Heap k largest:  O(N * log K)

Space: O(N) for original heapify

"""
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(nums)  # O(N)
        self.k = k
        while self.min_heap and len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
    # TODO: we can discard input ... only keep heap size of k
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # O(log k)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # O(log k)
        # heap min heap ... so "kth largest" is first
        return self.min_heap[0]     # this is O(1)
