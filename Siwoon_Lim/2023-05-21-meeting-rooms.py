# Time complexity: O(n log n)
# Space Complexity: O(1)

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution(object):
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
