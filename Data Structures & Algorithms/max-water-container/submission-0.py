class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        start = 0
        end = len(heights) - 1
        for h in heights:
            width = end - start
            curr_a = min(heights[start], heights[end]) * width
            max_a = max(curr_a, max_a)
            if heights[start] > heights[end]:
                end -= 1
            else: 
                start += 1
        return max_a

        