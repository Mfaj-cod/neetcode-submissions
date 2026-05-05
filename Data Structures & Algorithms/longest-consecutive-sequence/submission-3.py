class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        sett = set(nums)
        longest_seq = 0
        
        for n in nums:
            if (n - 1) not in sett:
                length = 0

                while n + length in sett:
                    length += 1
                
                longest_seq = max(length, longest_seq)

        return longest_seq
                