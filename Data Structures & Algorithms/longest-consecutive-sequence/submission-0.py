class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        longest_seq = 0
        curr_seq = 1
        for i in range(n):
            if i == 0:
                continue
            
            if nums[i] == (nums[i-1] + 1):
                curr_seq += 1
            elif nums[i] == (nums[i-1]):
                pass
            else:
                curr_seq = 1
            
            longest_seq = max(longest_seq, curr_seq)

        return longest_seq