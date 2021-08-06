"""
Approach: Sort by start, initialize res with first interval, merge if start is within res[-1]
1. sort by start
2. put first interval in res
3. loop thru rest
    a. merge if start overlaps last res' end
    b. append current if no overlap

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by first element
                        # lamda function, given this element -> return this instead
        intervals.sort(key=lambda element : element[0])
        
        # initialize output, containing first interval
        res = [intervals[0]]
        
        # step thru rest of intervals
        for (start, end) in intervals[1:]:
            last_end = res[-1][1]
            
            # update last end if overlap
            if start <= last_end:
                res[-1][1] = max(res[-1][1], end)
            # no overlap
            else:
                res.append([start,end])
        return res
            
        