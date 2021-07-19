"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""

intervals = [[1, 4], [4, 5]]
if len(intervals) <= 1:
    print(intervals)
intervals.sort()
new_intervals = [intervals[0]]
for i in range(1, len(intervals)):
    if new_intervals[-1][1] >= intervals[i][0]:
        new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
    else:
        new_intervals.append(intervals[i])
print(new_intervals)
