"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding
column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:                                  Example 2:
Input: columnTitle = "A"                    Input: columnTitle = "AB"
Output: 1                                   Output: 28

Example 3:                                  Example 4:
Input: columnTitle = "ZY"                   Input: columnTitle = "FXSHRXW"
Output: 701                                 Output: 2147483647
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = dict(zip(letters, val))
        res = 0
        for ch in columnTitle:
            res = res*26 + d[ch]
        return res


"""
EXPLANATION:
It's easier to start with a different and, probably, easier problem. How to convert a string of digits to a number. 
Let's say, you're given '67' and you want to return 67. Sure you can do return int(s)
but if you are here for this, you don't want to be here. Let's assume, to make the explanation shorter, 
you can apply int() only to single digits but not to the whole number. You're given '67.'

Let's start reading this line element by element and initialise a variable res = 0 that will contain the final result.
We will put the integer value of the first string's element to res. Now res contains 6. Are we done with the string? 
No. Let's read the next character.
The next character is 7. If we just add 7 to res, we will get 13. It's not what we want. 
We want to take whatever is stored in res already, multiply it by ten and add seven. 
This way we will take six, turn it into 60, add 7, and resave into res. 
Are we done with the line? Yes. Then just return res.

Here is the whole thing encoded:
def str2num(s):
    res = 0
    for digit in s:
        res = res * 10 + int(digit)
    return res

But the secret is: NEVER USE RECURSION UNLESS IT'S A DFS PROBLEM. 
In real life, once you finally get that fat FAANG job, NEVER USE RECURSION.

Let's get back to 171. The idea here is the same with two differences:
    We will use a dictionary to create a mapping "character: number."
    We will use 26 instead of 10

def titleToNumber(s):
    res = 0
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    for ch in s:
        res = res * 26 + d[ch]
    return res

As you can see, res is calculated exactly the same way as in the first portion of code above. 
We just use 26 instead of 10, and d[ch] instead of int(s[0]).
"""