class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(ls):
            if len(ls)<=1:
                return ls
            combine = backtrack(ls[1:])
            for i in combine:
                if len(i+ls[0])==len(set(i+ls[0])):
                    combine+=[i+ls[0]]
            combine+=[ls[0]]
            return combine
        
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i])!=len(set(arr[i])):
                arr.pop(i)
        combine = backtrack(arr)
        ans = 0
        for i in combine:
            ans = max(ans, len(i))
            
        return ans