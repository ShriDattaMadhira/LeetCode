"""
Given the array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent
to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i],
otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the
special discount.
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new = [-99] * len(prices)
        for i in range(len(prices)):
            # print("I:", i)
            # print("J: ", end="")
            for j in range(i + 1, len(prices)):
                # print(j, end=" ")
                if prices[j] <= prices[i]:
                    new[i] = prices[i] - prices[j]
                    break
            if new[i] == -99:
                new[i] = prices[i]
            # print("")
        return new
