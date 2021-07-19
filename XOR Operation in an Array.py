"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start] * n
        # op = 0
        for i in range(n):
            nums[i] += 2 * i
            # op = op^(start + 2*i)
        return reduce(lambda x, y: x ^ y, nums)
