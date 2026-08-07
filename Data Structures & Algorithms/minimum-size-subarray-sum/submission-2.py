class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        minL = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minL = min(minL, r - l + 1)
                total -= nums[l]
                l += 1
            
        return 0 if minL == float('inf') else minL