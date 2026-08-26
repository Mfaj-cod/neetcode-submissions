class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum, minsum = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0

        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            
            total += n

            maxsum = max(maxsum, curmax)
            minsum = min(minsum, curmin)
            
        return max(maxsum, total - minsum) if maxsum > 0 else maxsum