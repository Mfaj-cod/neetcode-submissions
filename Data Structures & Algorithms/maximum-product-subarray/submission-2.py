class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = 0
        n = len(nums)
        l, r = 0, 1
        while r < n:
            res = max(res, nums[l], nums[r], (nums[l] * nums[r]))
            l += 1
            r += 1
        
        return res