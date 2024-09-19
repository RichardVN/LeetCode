class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0,1
        
        intervals.sort()
        res = []

        # interval = [start, end]
        for interval in intervals:
            # empty res, no overlap ... start is more than last interval's end
            if not res or interval[START] > res[-1][END]:
                res.append(interval)
            # ANY overlap ... we take the larger of the start intervals (handles both complete/partial overlap cases)
            else:
                res[-1][END] = max(interval[END], res[-1][END])


        return res
