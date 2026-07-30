class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mapp = list(set(nums))

        for i, n in enumerate(mapp):
            nums[i] = n

        return len(mapp)