class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # recursive functions
        def dfs(i: int, total: int) -> int:
            if i == len(nums):
                return total
            # choosing an element once and not choosing once
            return dfs(i+1, total ^ nums[i]) + dfs(i+1, total)

        return dfs(0, 0)