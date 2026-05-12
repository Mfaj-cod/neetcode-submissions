class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        n = len(s)
        longest = 1
        curr = 0

        for r in range(n):
            if s[r] not in hashset:
                curr += 1
                hashset.add(s[r])
            else:
                curr = 1
            longest = max(longest, curr)

        return longest