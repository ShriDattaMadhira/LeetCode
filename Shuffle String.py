"""
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sl = [''] * len(indices)
        # j = 0
        for i, c in zip(indices, s):
            sl[i] = c
            # j += 1
        return ''.join(sl)
