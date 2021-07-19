"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
that are not part of the primary diagonal.
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        else:
            p_sum, s_sum, n = 0, 0, len(mat)
            for i in range(n):
                p_sum += mat[i][i]
                s_sum += mat[n - i - 1][i]

            if n % 2 != 0:
                s_sum -= mat[n // 2][n // 2]

            return p_sum + s_sum
