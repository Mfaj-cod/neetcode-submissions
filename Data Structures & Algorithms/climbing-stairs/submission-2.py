class Solution:
    def climbStairs(self, n: int) -> int:
        # DP - Bottom-Up (Tabulation)
        if n <= 2:
            return n

        tb = [0] * (n + 1)
        tb[1], tb[2] = 1, 2

        for i in range(3, n + 1):
            tb[i] = tb[i - 1] + tb[i - 2]
        
        return tb[n]