"""
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each
indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:
    Increment all the cells on row ri.
    Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all
locations in indices.
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for j in range(n)] for i in range(m)]
        print(matrix)
        for i in indices:
            # r, c = ,
            for j in range(n):
                matrix[i[0]][j] += 1
            for j in range(m):
                matrix[j][i[1]] += 1
        count = 0
        for i in matrix:
            for j in i:
                if j % 2 != 0:
                    count += 1
        return count
