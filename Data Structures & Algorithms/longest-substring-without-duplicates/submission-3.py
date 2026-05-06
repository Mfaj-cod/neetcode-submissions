class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        n = len(s)
        longest = 0
        l = 0

        for r in range(n):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            longest = max(longest, r - l + 1)

        return longest