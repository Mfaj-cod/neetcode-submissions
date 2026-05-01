class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # BubbleSort
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-1, i, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    swapped = True

        return nums