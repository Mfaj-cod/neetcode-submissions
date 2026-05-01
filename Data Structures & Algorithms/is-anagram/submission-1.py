class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)

        if len(s)==len(t):
            for el in t:
                if el not in s_set:
                    return False

        return True