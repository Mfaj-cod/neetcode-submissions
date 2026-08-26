class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        Target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i: int, k: int, subsetSum: int):
            if k == 0:
                return True
            if subsetSum == Target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or (subsetSum + nums[j]) > Target:
                    continue
                used[j] = True

                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True

                used[j] = False
            return False
        
        return backtrack(0, k, 0)