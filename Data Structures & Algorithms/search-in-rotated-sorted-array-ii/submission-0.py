class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        new, arr = set(nums), []

        return target in set(nums)
        # for item in new:
        #     arr.append(item)

        # n, k = len(arr), len(arr)
        # for i in range(1, n):
        #     if arr[i] < arr[i-1]:
        #         k = i

        # arr = nums[k:] + nums[:k]
        # l, r = 0, n - 1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if arr[mid] == target:
                