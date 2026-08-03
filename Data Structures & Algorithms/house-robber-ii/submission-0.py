class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - O(1) space
        if len(nums) == 1:
            return nums[0]
        
        def robb(nums: List[int]):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob2, rob1 + n)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(robb(nums[:-1]), robb(nums[1:]))