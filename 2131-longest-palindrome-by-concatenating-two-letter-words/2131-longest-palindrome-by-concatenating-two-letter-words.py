class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        table = {}
        ans = 0
        flag = 0
        ls = []
        for w in set(words):
            table[w] = words.count(w)
        for k,v in table.items():
            if k in ls:
                continue
            elif k[0]==k[1]:
                if flag==0 and v%2==1:
                    flag=1
                    ans+=2
                ans+=floor(v/2)*4
            elif k[::-1] in table:
                ans+=min(v, table[k[::-1]])*4
                ls += [k[::-1]]
        return ans          