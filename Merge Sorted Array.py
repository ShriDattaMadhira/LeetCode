"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

# Method - 1 : Using python libraries
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3
nums1[m:] = nums2[:n]
nums1.sort()
print("Method-1: ", nums1)

# Method-2 : Mergesort like code.
"""
The trick here is to arrange the elements from right hand side or back because there are empty spaces at the back of the
array. 
If we start from left, everytime a nums2 element is inserted the entire array needs to be shifted right. 
"""
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3
writeIndex = m+n-1  # The last index of the combined array.
while m > 0 and n > 0:
    if nums1[m-1] >= nums2[n-1]:
        nums1[writeIndex] = nums1[m-1]
        m -= 1
    else:
        nums1[writeIndex] = nums2[n-1]
        n -= 1
    writeIndex -= 1
if n > 0:
    nums1[:n] = nums2[:n]

print("Method-2: ", nums1)
