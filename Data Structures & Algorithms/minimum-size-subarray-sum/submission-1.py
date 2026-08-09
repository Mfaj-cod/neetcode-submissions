class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
            
        minL = float('inf')
        l, r = 0, 1
        while l < r and r < len(nums):
            if nums[l] >= target or nums[r] >= target:
                return 1
            elif sum(nums[l:r+1]) >= target:
                minL = min(minL, r - l + 1)
                l += 1
            else:
                r += 1
        
        return minL if minL < float('inf') else 0