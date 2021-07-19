"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years
of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's
population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        res = 0
        for log in logs:
            years[log[0] - 1950] += 1
            years[log[1] - 1950] -= 1

        for i in range(1, 101):
            years[i] += years[i - 1]
            if years[i] > years[res]:
                res = i
        return res + 1950
