class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini = len(s)+1  # minimum substring length
        ans = ''
        table = {}
        capacity = len(t)
        init = 10**5+1
        for ele in set(t):
            table[ele] = [init]*t.count(ele) 
        start = None
        end = None
        for i,char in enumerate(s):
            if char in table:
                replace_idx_t = -1
                mini_idx_s = i
                try:
                    j = table[char].index(init)
                    if start==None: 
                        start=i
                    table[char][j] = i
                    capacity-=1
                except:
                    j = table[char].index(min(table[char]))
                    if table[char][j]==start:
                        table[char][j] = i
                        start= init
                        for k,v in table.items():
                            start = min(min(v),start)
                    else:
                        table[char][j] = i
                        
                if capacity==0:
                    end = i+1
                    if end-start<mini:
                        ans = s[start:end]
                        mini = end-start
        
        return ans