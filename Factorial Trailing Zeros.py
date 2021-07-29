"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 5
        res = 0
        while x <= n:
            res += n // x
            x *= 5
        return res
