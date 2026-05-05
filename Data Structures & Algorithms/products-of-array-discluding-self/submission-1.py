class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        prefix = 1
        for i in range(n):
            if i == 0:
                res.append(prefix)
                continue

            prefix *= nums[i - 1]
            res.append(prefix)

        suffix = 1
        prod = 1
        for i in range(n-1, -1, -1):
            if i == (n - 1):
                res[i] = res[i] * suffix
                continue

            suffix *= nums[i + 1]
            prod = res[i] * suffix
            res[i] = prod

        return res