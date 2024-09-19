"""
Time: O(N) to iterate thru intervals
Space: O(N) to create res array
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Constant to help us access start and end indices of interval
        START, END = 0, 1

        # arrays that hold any intervals that do NOT overlap with newInterval, on left and right
        left, right = [], []
        
        # markers for newInterval  -- updates on any needed merges
        s, e = newInterval[START], newInterval[END]
    
        for interval in intervals:
            # interval segment is completely before
            if interval[END] < s:
                left.append(interval)
            # interval segment is completely after
            elif interval[START] > e:
                right.append(interval)
            # there is some overlap. we cannot append interval yet
            else:
                s = min(s, interval[START]) #TODO: remember to compare to markers, not original newInterval
                e = max(e, interval[END])

        return left + [ [s,e] ] + right