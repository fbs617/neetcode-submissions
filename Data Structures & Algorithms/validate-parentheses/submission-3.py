class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pars = { "(" : ")",
                 "{" : "}",
                 "[" : "]" }
        for c in s:
            if c in pars:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if c != pars[curr]:
                    return False
        if len(stack) == 0:
            return True
        return False

            