class Solution:
    def numDecodings(self, s: str) -> int:
        # DP - Top-Down (Memoization)
        n = len(s)
        cache = { n:1 }

        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1) < n and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"): # 0123456, because limit is 26 letters
                res += dfs(i + 2)
            
            cache[i] = res
            return res
        
        return dfs(0)
