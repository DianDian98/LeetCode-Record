class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = [i for i in range(len(grid[0]))]
        for j in range(len(ans)):
            for row in grid:
                try:
                    if row[ans[j]]!=row[ans[j]+row[ans[j]]]:
                        ans[j]=-1
                        break
                except:
                    pass
                ans[j]+=row[ans[j]]
                if ans[j]<0 or ans[j]>len(ans)-1:
                    ans[j]=-1
                    break
        return ans