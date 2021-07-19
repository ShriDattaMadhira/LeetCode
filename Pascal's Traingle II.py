"""
Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the Pascal's triangle.
"""


# Method-2: DP
rowIndex = 3
dp = [0] * (rowIndex + 1)
dp[0] = 1
for i in range(1, rowIndex + 1):
    prev = 1
    for j in range(1, i + 1):
        nex_prev = dp[j]
        dp[j] = prev + dp[j]
        prev = nex_prev
    print(dp)
print(dp)
