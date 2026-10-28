class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy_price = prices[0]

        for index in range(1, len(prices)):

            current_day_price = prices[index]
            if current_day_price >= buy_price:
                max_profit += (current_day_price - buy_price)
            
            buy_price = current_day_price
        
        return max_profit
        