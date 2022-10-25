class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1]<intervals[i][0]:
                ans+=[intervals[i]]
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans