class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        table = {}
        
        for w in words:
            if w not in table:
                table[w]=1
            else:
                table[w]+=1
        print(sorted(table.items()))
        table = sorted(sorted(table.items()), key=lambda x:x[1],reverse=True)
        
        return [table[i][0] for i in range(k)]