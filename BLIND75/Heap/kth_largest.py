"""
Approach Heap:
    - heap k size
    - go thru rest of nums, heappushpop  ... pop out minimum n-k times
    
Time: O( N * log k)    O(log k) to add to heap size k, we do N times possibly
Space :  O(k) for heap

"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initial heap
        heap = nums[:k]
        # O(k)
        heapq.heapify(heap)
        for num in nums[k:]:
            # POP SMALLEST n-k times
            heapq.heappushpop(heap, num)
        # left with kth largest element at top of heap
        return heap[0]