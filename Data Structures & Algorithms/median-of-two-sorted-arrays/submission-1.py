class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged = sorted(nums1 + nums2)
        merged = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1
        
        if l < len(nums1):
            merged += nums1[l:]
        if r < len(nums2):
            merged += nums2[r:]

        if len(merged) % 2 == 0:
            mid = len(merged) // 2
            mid2 = mid - 1
            return (merged[mid] + merged[mid2]) / 2
            
        mid = len(merged) // 2
        return merged[mid]