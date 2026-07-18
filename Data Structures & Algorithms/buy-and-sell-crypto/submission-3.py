class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(len(prices)):
            # Update minimum price seen so far
            if prices[i] < min_price:
                min_price = prices[i]
            
            # Calculate profit if we sell today
            profit = prices[i] - min_price
            
            # Update max profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit







        # left = 0
        # right = 1
        # max_profit = 0
        
        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         profit = prices[right] - prices[left]
        #         if profit > max_profit:
        #             max_profit = profit
        #     else:
        #         left = right  # Found lower price
            
        #     right = right + 1
        
        # return max_profit






        # for i in range(len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         curr_diff = prices[j] - prices[i]
        #         max_profit = max(max_profit, curr_diff)
        # return max_profit