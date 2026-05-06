class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ')': '(', '}': '{', ']': '[' }
        stk = []

        for c in s:
            if c in hashmap:
                if stk and stk[-1] == hashmap[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False