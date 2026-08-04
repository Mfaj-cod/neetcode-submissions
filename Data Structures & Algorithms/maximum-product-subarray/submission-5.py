class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax * n
            currMax = max(n, n*currMax, n*currMin)
            currMin = min(n, temp, n*currMin)

            res = max(res, currMax)
        
        return res
