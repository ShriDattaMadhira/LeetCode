"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
            # j = i
            for j in range(i, len(arr), 2):
                # print(arr[i:j+1])
                # j += 2
                s += sum(arr[i:j + 1])
                # break
        return s
