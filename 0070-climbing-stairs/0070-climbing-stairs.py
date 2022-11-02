class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1,2]
        for i in range(2,n):
            ans+=[ans[i-2]+ans[i-1]]
        return ans[n-1]