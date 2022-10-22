class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini = len(s)+1    # minimum substring length
        ans = ''
        table = {}         # ans possible index
        capacity = len(t)  # table capacity
        init = 10**5+1     # initialize
        
        # create initial table  
        for ele in set(t):
            table[ele] = [init]*t.count(ele) 
            
        start, end = None, None
        for i,char in enumerate(s):
            if char in table:
                try:   # table has init
                    j = table[char].index(init)
                    table[char][j] = i
                    capacity-=1
                    if start==None:  start=i   # initial start       
                except:
                    j = table[char].index(min(table[char]))
                    if table[char][j]==start:  # 如果start要被取代，重找start 
                        table[char][j] = i
                        start= init
                        for k,v in table.items():
                            start = min(min(v),start)
                    else:
                        table[char][j] = i
                        
                if capacity==0:  # table is filled
                    end = i+1
                    if end-start<mini:
                        ans = s[start:end]
                        mini = end-start
        
        return ans