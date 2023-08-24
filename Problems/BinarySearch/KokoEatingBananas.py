"""
TODO:  The possible eating rates (k) are in range [1 .... max_pile_size]
    - instead of trying every rate: use binary search to find middle rate
    - if valid k, update answer and Try smaller rate. Else try larger rate.

"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper function: is it possible finish bananas at rate k?
        def isEatable(k):
            hrs = [math.ceil(pile / k) for pile in piles]   # TODO: use / float division so we can round up
            return sum(hrs) <= h

        # possible rates are 1 through max_pile size
        # imagine [1 .... max_pile]

        min_k = max(piles)

        l = 0
        r = max(piles)
        while l <= r:
            k = l + (r-l)// 2
            if isEatable(k):
                min_k = min(min_k, k)   # possible rate. Update answer
                r = k - 1               # try for smaller k
            else:
                l = k + 1       # not possible, need larger k

        # worst case, min_k is max pile size
        return min_k 