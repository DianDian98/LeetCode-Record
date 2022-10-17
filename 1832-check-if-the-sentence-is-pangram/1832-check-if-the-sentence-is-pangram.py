class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for alphabet in range(0,26):
            if chr(alphabet+ord('a')) not in sentence:
                return False
        
        return True