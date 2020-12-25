# O(N)
import unittest
from collections import Counter

"""
NOTE:
    - Whitespace and non-letter characters do not matter
    - Characteristic of palindrome: Each char (except maybe one) has an even parity
Intuition:
    - Step through string and add char to hash map if it is a char. Increment counts
    - Step through hash map, if there is more than one odd parity, it is not palindrome

"""
def is_palindrome_permutation(phrase):
    """checks if a string is a permutation of a palindrome"""

    char_count = dict()
    odd_parity_seen = False
    for c in phrase:
        # Casing DOES NOT MATTER
        c = c.lower()
        if c.isalpha():
            if c in char_count:
                char_count[c] += 1
            else: 
                char_count[c] = 1
    
    for val in char_count.values():
        if val % 2 != 0:
            # we have more than one odd parity
            if odd_parity_seen:
                return False
            # set flag for seeing one odd parity
            else:
                odd_parity_seen = True
    return True

    # table = [0 for _ in range(ord("z") - ord("a") + 1)]
    # countodd = 0
    # for c in phrase:
    #     x = char_number(c)
    #     if x != -1:
    #         table[x] += 1
    #         if table[x] % 2:
    #             countodd += 1
    #         else:
    #             countodd -= 1

    # return countodd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [is_palindrome_permutation, is_palindrome_permutation_pythonic]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
