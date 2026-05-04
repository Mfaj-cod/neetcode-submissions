class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            # If mid is greater than right, min is in the right half
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, min is at mid or in the left half
            else:
                r = m
                
        return nums[l]