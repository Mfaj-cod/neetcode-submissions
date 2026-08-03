class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def sub(l: int, r: int) -> int:
            curr = 0
            while l >= 0 and r < n and s[l] == s[r]:
                curr += 1
                l -= 1
                r += 1
            return curr
        
        for i in range(n):
            # for odd length
            res += sub(i, i)
            # for even length
            res += sub(i, i+1)
        
        return res