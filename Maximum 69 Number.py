"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        l = []
        for d in str(num):
            l.append(d)
        for i in range(len(l)):
            if l[i] == '6':
                l[i] = '9'
                break
        return int(''.join(l))
