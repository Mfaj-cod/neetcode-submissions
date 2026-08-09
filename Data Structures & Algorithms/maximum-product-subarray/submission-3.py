class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = 0
        n = len(nums)

        l, r = 0, 1
        while r < n:
            prod = nums[l]
            for p in range(l+1, r+1):
                prod *= nums[p]
                
            if prod > res:
                res = prod
            elif prod <= res:
                l += 1
            r += 1
        return res