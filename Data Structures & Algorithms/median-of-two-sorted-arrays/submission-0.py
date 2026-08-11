class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        if len(merged) % 2 == 0:
            mid = len(merged) // 2
            mid2 = mid - 1

            return (merged[mid] + merged[mid2]) / 2
        else:
            mid = len(merged) // 2
            return merged[mid]