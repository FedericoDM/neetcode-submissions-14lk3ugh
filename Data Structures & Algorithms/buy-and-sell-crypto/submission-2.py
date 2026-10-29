class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Make max profit
        """
        # Ensure no prices are the same:
        if len(set(prices)) == 1:
            return 0

        profits = []
        for index in range(len(prices)):
            if index < len(prices) - 1:
                buying_price = prices[index]
                remaining_prices = [
                    price for price in prices[index + 1:] if price > buying_price 
                ]
                print(f"Buying price: {buying_price}, remaining {remaining_prices}")
                if remaining_prices:
                    profit = max(remaining_prices) - buying_price
                    profits.append(profit)
                else:
                    continue

        if profits:
            return max(profits)

        else:
            return 0
                


