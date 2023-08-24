"""
* Construct a min-heap of 'started' meetings that are occupying a room. key= end_time
    Top of heap = earliest ending meeting

1. Sort meetings by START time. We should give rooms to earlier meetings first.
2. Process a Meeting
    a. IF this meeting's start time is AFTER heap's earliest ending meeting, pop heap... "use an existing free meeting room instead of making a new one"
    b. Always add current meeting to heap, signify it is taking a room now
3. return size of heap
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        neededRooms = 0

        # sort by meeting START
        intervals.sort(key=lambda interval:interval[0])
        
        # heap of 'started' meetings END times. Starts only one, no need to heapify
        started_meetings = [intervals[0][1]]

        # loop thru remaining meetings
        for meeting_start, meeting_end in intervals[1:] :
            # check if earliest ending meeting is done. Then we can replace them
            if started_meetings[0] <= meeting_start:  #TODO: if times ==, we still replace
                heapq.heappop(started_meetings)

            # 'start' meeting
            heapq.heappush(started_meetings, meeting_end)
        
        # return len of heap. Concurrent meetings
        return len(started_meetings)

