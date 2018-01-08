
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        newi = []
        intervals = sorted(intervals, key = lambda asd:asd.start, reverse=False)
        for i in range(len(intervals)):
            if i == 0:
                pass
            else:
                if intervals[i-1].end < intervals[i].start:
                    newi.append(intervals[i-1])
                elif intervals[i-1].end >intervals[i].end:
                    intervals[i].start = intervals[i-1].start
                    intervals[i].end = intervals[i-1].end
                else:
                    intervals[i].start = intervals[i - 1].start
        if len(intervals)!=0:
            newi.append(intervals[-1])

        return newi

s= Solution()
i1 = Interval(1,4)
i2 = Interval(0,4)
i = []
i.append(i1)
i.append(i2)
s.merge(i)