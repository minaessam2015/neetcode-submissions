class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        window_size = 1
        start, end = 0, 1
        max_profit = 0
        while end < len(prices):
            if prices[end] - prices[start] < 0:
                # start a new window
                start = end
               
            elif prices[end] - prices[start] > max_profit:
                    max_profit = prices[end] - prices[start]
            end += 1
        return max_profit
                
        