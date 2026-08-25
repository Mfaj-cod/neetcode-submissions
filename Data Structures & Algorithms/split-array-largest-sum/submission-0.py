class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, m):
            if m == 1:
                return sum(nums[i:])
            if (i, m) in dp:
                return dp[(i, m)]

            res = float("inf")
            curSum = 0
            for j in range(i, n - m + 1):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))
                if curSum > res:
                    break
            
            dp[(i, m)] = res
            return res

        return dfs(0, k)