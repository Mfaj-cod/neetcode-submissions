class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = -1
        for i in range(n):
            nums1[x] = nums2[i]
            x -= 1
        
        nums1.sort()

        

        

        