class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        hashmap = dict()
        for ch in s:
            hashmap[ch] = ord(ch)

        for i in range(len(s)-1):
            mod = abs(hashmap.get(s[i]) - hashmap.get(s[i+1]))
            res += mod

        return res