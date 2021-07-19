"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m = c = 0
        for i in s:
            if i == 'L': c += 1
            if i == 'R': c -= 1
            if c == 0: m += 1
        return m