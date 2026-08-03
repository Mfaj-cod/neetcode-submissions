class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        n = len(s)

        def longestP(l, r):
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                r += 1
                l -= 1

        for i in range(n):
            # for odd length
            longestP(i, i)
            # for even length
            longestP(i, i+1)
            
        return res
    