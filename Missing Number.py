nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# nums = [4, 3, 6, 2, 1, 1]
sum_N = (len(nums) * (len(nums) + 1) // 2)
sum_N2 = (len(nums) * (len(nums) + 1) * (2 * len(nums) + 1) // 6)
missing = sum_N - sum(nums)  # If there are no duplicates.
# missing = (sum_N + sum_N2 // sum_N) // 2  # If there are duplicates.
print("Missing number: ", missing)
print("Repeating number: ", missing - sum_N)
