class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    result[j] = i - j
                else:
                    break
            stack.append(i)
        
        return result
