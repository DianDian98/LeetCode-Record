class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty)<d:
            return -1
        
        @cache
        def dp(i,ans,d):
            if len(jobDifficulty) == i and d == 0: return ans
            if len(jobDifficulty[i:])<d or d <= 0: return inf
            # min(繼續工作, 換天工作)
            return min(dp(i+1,max(ans,jobDifficulty[i]),d), max(ans,jobDifficulty[i])+dp(i+1,0,d-1))
            
        return dp(0,0,d)
                