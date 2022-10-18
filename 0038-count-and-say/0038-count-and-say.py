class Solution:
    
    def countAndSay(self, n: int) -> str:
        def say(num):
            if num==1: return '1'
            ans = ''
            for s in say(num-1):
                if ans=='' or ans[-1]!=s:
                    ans+='1'+s
                else:
                    ans=ans[:-2]+str(int(ans[-2])+1)+s      
            return ans                
                
        return say(n)