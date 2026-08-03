class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - Memoization
        cache = {}
        n = len(nums)

        def dfs(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        
        return dfs(0)