"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
ith customer has in the jthbank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = []
        for i in accounts:
            money = 0
            for j in i:
                money += j
            max_money.append(money)
        return max(max_money)