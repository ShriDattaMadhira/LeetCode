"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
import math


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = [nums[0]]
        for i in range(1, len(nums)):
            print(s)
            if nums[i] > s[-1]:
                s.append(nums[i])
            elif nums[i] <= s[0]:
                s[0] = nums[i]
            else:
                start, end = 0, len(s) - 1
                while start <= end:
                    mid = math.ceil((start + end) / 2)
                    if nums[i] == s[mid]:
                        break
                    elif nums[i] < s[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                mid = math.ceil((start + end) / 2)
                s[mid] = nums[i]

        print(s)
        return len(s)

