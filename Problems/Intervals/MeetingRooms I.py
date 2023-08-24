"""
Sort by start time
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2: return True
        # unable to attend if Start time is before any endtime 
        intervals.sort()

        for i in range(1, len(intervals)):
            endPrev = intervals[i-1][1]
            start = intervals[i][0]

            if start < endPrev:
                return False
        return True