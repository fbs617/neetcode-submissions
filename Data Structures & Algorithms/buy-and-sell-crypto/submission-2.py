class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right  # Found lower price
            
            right = right + 1
        
        return max_profit






        # for i in range(len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         curr_diff = prices[j] - prices[i]
        #         max_profit = max(max_profit, curr_diff)
        # return max_profit