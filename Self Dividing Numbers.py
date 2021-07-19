"""
A self-dividing number is a number that is divisible by every digit it contains.
    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for num in range(left, right + 1):
            if num < 10:
                l.append(num)
            else:
                temp = num
                flag = True
                while temp > 0:
                    check = temp % 10
                    if check == 0 or num % check != 0:
                        flag = False
                        break
                    temp //= 10
                if flag:
                    l.append(num)
        return l
