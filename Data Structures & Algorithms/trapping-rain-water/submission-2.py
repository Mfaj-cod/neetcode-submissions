class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        i = 0
        while i < n:
            if height[i] != 0:
                break
            i += 1

        j = i + 1

        while j < n:
            if height[i] > height[j]:
                res += (height[i] - height[j])

            if j+1 < n and height[j+1] > height[i]:
                i = j + 1
                j = i + 1

            if j+1 < n and height[j+1] < height[i]:
                res += (height[i] - height[j+1])
                i += 1
            j += 1
        
        return res
