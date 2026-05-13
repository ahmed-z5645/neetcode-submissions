"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda x: x.start)

        for i in range(0, len(intervals) - 1):
            f = intervals[i]
            s = intervals[i + 1]

            if s.start < f.end:
                return False
        
        return True