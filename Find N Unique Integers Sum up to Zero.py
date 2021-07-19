"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""


class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = [float("inf")]*n
        i, j = 0, 0
        if n == 1:
             return [0]
        elif n == 2:
            return [-1,1]
        elif n % 2 != 0:
            l[0] = 0
            n -= 1
            i += 1
        while i < n:
            l[i] = (j+1)
            l[i+1] = -(j+1)
            i += 2
            j += 1
        print(l)
        return l
