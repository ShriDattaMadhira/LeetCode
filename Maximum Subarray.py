"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.
"""

"""
Kadane's Algorithm
==================
** What is the maximum subarray that can be formed that is ending at index 'i'.
        Eg: [1, -3, 2, 1, -1]
            subarrays ending at index0 or 1 are [1] - Max of these is [1]
            subarrays ending at index1 or -3 are [-3], [1, -3] - Max of these is [1, -3]
            subarrays ending at index2 or 2 are [2], [-3, 2], [1, -3, 2] - Max of these is [2] and so on
** Repeat the same step until you get max subarrays possible at each index.
** Now, we compare them, to get the maximum subarray of the array.

** But this process is still going to take O(n^2).
** To complete the algorithm below O(n), we have an interesting idea. It is, 
        THE MAXIMUM SUBARRAY AT CURRENT INDEX IS EITHER THE ELEMENT ITSELF OR THE CURRENT ELEMENT ADDED TO THE MAXIMUM 
        SUBARRAY UNTIL THIS POINT (i.e., MAXIMUM SUBARRAY OF THE PREVIOUS ELEMENT).
"""
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_curr, max_global, max_subarray = nums[0], nums[0], [nums[0]]
# Write the code for printing the subarray.
for i in range(1, len(nums)):
    max_curr = max(nums[i], max_curr+nums[i])
    if max_curr > max_global:
        max_global = max_curr
        # max_subarray = temp_array
print("Max Sum of Subarray is: ", max_global)
