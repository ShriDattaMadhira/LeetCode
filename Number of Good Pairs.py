"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        c = 0
        for i in nums:
            if i in count:
                c += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return c