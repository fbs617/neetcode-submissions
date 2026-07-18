class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        stack = []
        while (i < len(asteroids)):
            ast = asteroids[i]
            if ast > 0:
                stack.append(ast)
                i += 1
            elif not stack or stack[-1] < 0:
                stack.append(ast)
                i += 1
            elif stack[-1] == (-1 * ast):
                stack.pop()
                i += 1
            elif stack[-1] < (-1 * ast):
                stack.pop()
            else:
                i += 1
        return stack






            # if (ast < 0) and stack:
            #     to_compare = stack[-1]
            #     if to_compare < 0:
            #         stack.append(to_compare)
            #         i += 1
            #     elif ast + to_compare == 0:
            #         stack.pop()
            #         i += 1
            #     elif ast + to_compare < 0:
            #         stack.pop()
            # elif (ast > 0):
            #     stack.append(ast)
            #     i += 1
        # return stack
            
            