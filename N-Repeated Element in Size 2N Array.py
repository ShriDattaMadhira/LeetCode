"""
In a array nums of size 2 * n, there are n + 1 unique elements, and exactly one of these elements is repeated n times.

Return the element repeated n times.
"""


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # nums_set = set(nums)
        for num in nums:
            if nums.count(num) == len(nums) / 2:
                return num
