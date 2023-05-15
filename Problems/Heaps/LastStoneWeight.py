"""
TODO:
- every time push into heap, make sure its negative
- every time pop, or access heap... convert back to positive

Pseudo:
- heapify O(N)
- while 2 or more stones:
    - heappop the two heaviest
    - compare.. if unequal heappush() the remainder weight
- return whats left in stones

TIME: (N log N)  ... each pop is log N
SPACE: O(1)  heapify modifies array in place, modifies array
"""

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # neg, so we can do "max heap"
        stones = [- stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            # s1 is heaviest
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                new = - (abs(s1) - abs(s2))
                heapq.heappush(stones, new)
        return abs(stones[0]) if stones else 0