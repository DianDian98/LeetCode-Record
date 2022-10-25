class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort_intervals = sorted(intervals, key = lambda intervals : intervals[1])
        # ans = []
        intervals = sorted(intervals)
        for i in range(len(intervals)):
            if i==0:
                ans = [intervals[i]]
            elif ans[-1][1]<intervals[i][0]:
                ans+=[intervals[i]]
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans
                