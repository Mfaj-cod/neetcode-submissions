class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mapp = list(set(nums))
        mapp.sort()

        for i, n in enumerate(mapp):
            nums[i] = n

        return len(mapp)