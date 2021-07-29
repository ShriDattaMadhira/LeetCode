"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, best_buy = 0, prices[0]
        for price in prices:
            if price < best_buy:
                best_buy = price
            elif price > best_buy:
                if max_profit < price-best_buy:
                    max_profit = price-best_buy
        return max_profit


"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best = 0
        for price in prices[1:]:
            if price > best_buy:
                best += price-best_buy
            best_buy = price
        return best


"""

"""