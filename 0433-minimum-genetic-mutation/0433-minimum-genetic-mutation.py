class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ans = 0
        record = []
        ls = [start]
        while ls!=[]:
            print(ls)
            nex = []
            for gene in ls:
                if gene==end: return ans
                for i in range(len(gene)):
                    for c in 'ACGT':
                        tmp = gene[:i]+c+gene[i+1:]
                        print(tmp)
                        if tmp in bank and tmp not in record:
                            nex+=[tmp]
                            record+=[tmp]
            ans+=1
            ls = nex
        print('\n')    
        return -1