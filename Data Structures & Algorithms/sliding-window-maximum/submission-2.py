class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k >= len(nums):
            return [max(nums)]
        
        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left ind from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res