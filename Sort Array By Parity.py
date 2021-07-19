"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums,
followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # op = [0]*len(nums)
        # i,j = 0, len(nums)-1
        # for num in nums:
        #     if num%2 == 0:
        #         op[i] = num
        #         i += 1
        #     else:
        #         op[j] = num
        #         j -= 1
        # return op

        # nums.sort(key = lambda x : x%2)
        # return nums

        e, o = [], []
        for num in nums:
            if num % 2 == 0:
                e.append(num)
            else:
                o.append(num)
        e.extend(o)
        return e