"""
NOTE: sorted already
Approach:  Step thru each interval and compare new interval.
    - if new interval's begin is after current's end:  append current
    - if new interval's end is before current's begin:  append new and rest of intervals. return
    - else:  there is overlap:   merge interval into new interval
    
    - append new interval and return res

Time: O(N), already sorted
Space: O(N) for res

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        # iterate thru each interval
        for i in range(len(intervals)):
            # if new interval completely past current interval, append current interval to res
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                # DONT return yet, dont know where put new interval
            # if ending of new interval comes before beginning of current interval
            elif newInterval[1] < intervals[i][0]:
                # append new interval and remaining intervals and return res
                res.append(newInterval)
                return res + intervals[i:]
                
            
            # else: there is overlap beteen new and current. MERGE into new interval
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                
        # add merged interval to result if first if never exectues
        res.append(newInterval)
        
        return res