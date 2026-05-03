class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        f, s = 0, 0

        while f < len(word1) and s < len(word2):
            res += word1[f]
            res += word2[s]

            f += 1
            s += 1
        
        while f < len(word1):
            res += word1[f]
            f += 1
        while s < len(word2):
            res += word2[s]
            s += 1

        return res