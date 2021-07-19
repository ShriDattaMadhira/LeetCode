"""
Sort an array of 0’s 1’s 2’s without using extra space or sorting algo

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

# Method - 1 : Using counting sort, O(n), two passes through an array.
counter = [0]*3
nums = [1, 2, 0]
for num in nums:
    counter[num] += 1
index = 0
for i in range(len(counter)):
    while counter[i] > 0:
        nums[index] = i
        index += 1
        counter[i] -= 1
print("Method-1:", nums)

# Method - 2: Dutch National Flag Problem or 3-way partitioning Quick Sort Algorithm
"""
Linear time partition routine
Seperates the values into three groups:
    a. Values less than the pivot
    b. Values equal to the pivot
    c. Values greater than the pivot
"""
nums = [1, 2, 0]
start, mid, end = 0, 0, len(nums)-1
pivot = 1
while mid <= end:
    if nums[mid] < pivot:
        nums[start], nums[mid] = nums[mid], nums[start]
        start += 1
        mid += 1
    elif nums[mid] > pivot:
        nums[mid], nums[end] = nums[end], nums[mid]
        end -= 1
    else:
        mid += 1
print("Method-2:", nums)




