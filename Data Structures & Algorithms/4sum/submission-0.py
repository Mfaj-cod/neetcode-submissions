class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        # Outer pointers must explore every unique pair of boundaries
        l = 0
        while l < n - 3:
            # Skip duplicates for the first element
            if l > 0 and nums[l] == nums[l-1]:
                l += 1
                continue
                
            r = n - 1
            while r > l + 2:
                # Skip duplicates for the second element (moving backwards)
                if r < n - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                # Inner two-pointer logic
                x, y = l + 1, r - 1
                while x < y:
                    fourSum = nums[l] + nums[r] + nums[x] + nums[y]
                    if fourSum < target:
                        x += 1
                    elif fourSum > target:
                        y -= 1
                    else:
                        res.append([nums[l], nums[x], nums[y], nums[r]])
                        x += 1
                        y -= 1
                        # Skip duplicates for the inner pointers
                        while x < y and nums[x] == nums[x-1]:
                            x += 1
                        while x < y and nums[y] == nums[y+1]:
                            y -= 1
                
                # Step 'r' independently to try the next right boundary
                r -= 1
            
            # Step 'l' independently to try the next left boundary
            l += 1
        
        return res
