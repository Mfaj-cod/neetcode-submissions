class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        self = 0
        while self < n:
            mult = 1
            for i in range(n):
                if i == self:
                    continue
                mult *= nums[i]
            res.append(mult)
            self += 1

        return res