class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def fun(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return fun(i+1, j+1)
            return fun(i, j+1)

        return fun(0, 0)