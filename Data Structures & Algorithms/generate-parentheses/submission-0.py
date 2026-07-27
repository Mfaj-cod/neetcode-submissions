class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranth. if open < close.
        # only add close paranth. if closed < open.
        # valid ones will have open==closed==n
        res = []
        stk = []

        def bktk(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stk))
                return
            
            if openN < n:
                stk.append("(")
                bktk(openN + 1, closedN)
                stk.pop()
            
            if closedN < openN:
                stk.append(")")
                bktk(openN, closedN + 1)
                stk.pop()
        bktk(0, 0)
        return res