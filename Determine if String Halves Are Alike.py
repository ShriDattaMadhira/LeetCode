"""
You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


import math

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ["a", "e", "i", "o", "u"]
        mid = math.ceil(len(s)/2)
        # a, b = s[:mid], s[mid:]
        count = 0
        for letter in s[:mid]:
            if letter in vowels:
                count += 1
        for letter in s[mid:]:
            if letter in vowels:
                count -= 1
        if count == 0:
            return True
        else:
            return False
