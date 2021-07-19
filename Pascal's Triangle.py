"""
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        for row in range(2, numRows):
            temp = [1] * (row + 1)
            for r in range(1, row):
                temp[r] = pascal[row - 1][r] + pascal[row - 1][r - 1]
            pascal.append(temp)
        print(pascal)
