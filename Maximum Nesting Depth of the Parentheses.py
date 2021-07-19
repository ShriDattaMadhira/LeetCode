"""
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

    It is an empty string "", or a single character not equal to "(" or ")",
    It can be written as AB (A concatenated with B), where A and B are VPS's, or
    It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

    depth("") = 0
    depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
    depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
    depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        # print(s.split("("))
        if len(s.split("(")) == 1 or len(s) == 0:
            return 0
        else:
            count = 0
            max_no = 0
            for i in s:
                if i == "(":
                    count += 1
                    if count > max_no:
                        max_no = count
                elif i == ")":
                    count -= 1

            return max_no
