class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        s = s.strip()
        n = len(s) - 1

        while n >= 0:
            if s[n] == ' ':
                break
            res += 1
            n -= 1

        return res
        