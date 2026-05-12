class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for e in s:
            if e=='(' or e=='{' or e=='[':
                stk.append(e)
            else:
                if stk:
                    last = stk.pop()
                    if e=='(' and last!=')':
                        return False
                    elif e=='{' and last!='}':
                        return False
                    elif e=='[' and last!=']':
                        return False

        return True