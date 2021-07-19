"""
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.
You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break,
and any egg dropped at or below floor f will not break.
Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks,
you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the minimum number of moves that you need to determine with certainty what the value of f is.
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        q = 300
        eggFloor = [[0 for j in range(k + 1)] for i in range(q + 1)]
        temp = 0
        for i in range(1, q + 1):
            for j in range(1, k + 1):
                eggFloor[i][j] = 1 + eggFloor[i - 1][j] + eggFloor[i - 1][j - 1]
            if eggFloor[i][j] >= n:
                return i
