class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap = {"+":"+", "-":"-", "*":"-", "/":"/"}
        stack = []

        for t in tokens:
            if t not in hashmap:
                stack.append(int(t))
            else:
                if t=="+":
                    last = stack.pop()
                    second_last = stack.pop()

                    stack.append(second_last + last)
                elif t=="-":
                    last = stack.pop()
                    second_last = stack.pop()

                    stack.append(second_last - last)
                elif t=="*":
                    last = stack.pop()
                    second_last = stack.pop()

                    stack.append(second_last * last)
                elif t=="/":
                    last = stack.pop()
                    second_last = stack.pop()

                    stack.append(second_last // last)

        return stack[-1] if stack else None