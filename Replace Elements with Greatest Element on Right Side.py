"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g = [-1] * len(arr)
        greatest = -999
        for i in range(len(arr) - 1):
            greatest = max(arr[i + 1:])
            g[i] = greatest
        g[-1] = -1
        return g
