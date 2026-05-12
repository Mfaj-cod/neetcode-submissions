class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1

        for n in nums:
            if n > 0:
                return n

