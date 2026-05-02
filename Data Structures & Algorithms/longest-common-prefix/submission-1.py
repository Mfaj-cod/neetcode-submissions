class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        c = 0
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                c = 0
                while c < len(strs[i]) and c < len(strs[j]):
                    if strs[i][c] != strs[j][c]:
                        return lcp
                    lcp += strs[i][c]
                    c += 1
        
        return lcp