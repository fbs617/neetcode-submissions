class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        i = 0
        j = 1
        max_p = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                curr_p = prices[j] - prices[i]
                max_p = max(max_p,curr_p)
                j += 1
            else:
                i = j
                j += 1
        return max_p
