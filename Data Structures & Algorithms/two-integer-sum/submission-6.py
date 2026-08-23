class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, n in enumerate(nums):
            if (target - n) in mapp:
                return [mapp[target - n], i]
            mapp[n] = i
        return []
            