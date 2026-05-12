class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 0, x//2
        ans = 1

        while l < r:
            m = l + (r - l) // 2
            m_sq = m * m
            if m_sq == x:
                return m
            elif m_sq > x:
                r = m - 1
            else:
                ans = m
                l = m + 1
        
        return ans
            