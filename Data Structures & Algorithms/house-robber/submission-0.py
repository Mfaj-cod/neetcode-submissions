class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = 0

        def dfs(i):
            if i >= len(nums):
                return 0
            
            money = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return money
        
        return dfs(0)