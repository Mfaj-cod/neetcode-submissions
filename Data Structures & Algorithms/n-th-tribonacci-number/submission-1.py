class Solution:
    def tribonacci(self, n: int) -> int:
        # DP (memoization)
        memo = {0:0, 1:1, 2:1}

        def f(x):
            if x in memo:
                return memo[x]
            memo[x] = f(x-1) + f(x-2) + f(x-3)
            return memo[x]
        
        return f(n)