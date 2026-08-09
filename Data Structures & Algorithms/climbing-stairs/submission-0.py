class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion solution
        def step(i):
            if i > n:
                return 0
            if i == n:
                return 1
            
            return step(i + 1) + step(i + 2)
        
        return step(0)
            