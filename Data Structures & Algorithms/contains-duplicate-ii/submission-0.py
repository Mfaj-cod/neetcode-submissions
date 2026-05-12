class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            if nums[l] == nums[r] and abs(l-r) <= k:
                return True
            l += 1
            r -= 1
        return False
