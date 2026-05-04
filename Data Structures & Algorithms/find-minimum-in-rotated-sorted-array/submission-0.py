class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_el = float("inf")
        for n in nums:
            min_el = min(n, min_el)

        return min_el