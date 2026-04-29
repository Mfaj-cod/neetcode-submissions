class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = dict(), dict()

        for e in s:
            s_map[e] = 1 + s_map.get(e, 0)
        for e in t:
            t_map[e] = 1 + t_map.get(e, 0)

        if s_map==t_map:
            return True

        return False