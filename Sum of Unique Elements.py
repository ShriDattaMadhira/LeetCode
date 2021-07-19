"""
You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            if nums.count(num) == 1:
                s += num
        return s
