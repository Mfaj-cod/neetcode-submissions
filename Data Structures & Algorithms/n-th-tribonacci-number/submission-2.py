class Solution:
    def tribonacci(self, n: int) -> int:
        # DP (Tabulation / Bottom-Up) with space O(1)
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1
            
        prev, curr, nxt = 0, 1, 1

        for i in range(3, n+1):
            prev, curr, nxt = curr, nxt, prev + curr + nxt

        return nxt