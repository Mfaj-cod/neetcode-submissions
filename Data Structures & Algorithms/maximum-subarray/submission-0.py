class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        
        maxsum = float('-inf')
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsum = max(cursum, maxsum)
        
        return maxsum