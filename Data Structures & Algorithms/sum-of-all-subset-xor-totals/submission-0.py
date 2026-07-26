class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def recurse(index: int, subset: List[int]):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr ^= num
            res += xorr

            for j in range(index, len(nums)):
                subset.append(nums[j])
                recurse(j + 1, subset)
                subset.pop()

        recurse(0, [])
        return res