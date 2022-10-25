class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''.join(w for w in word1)
        string2 = ''.join(w for w in word2)
        return string1==string2