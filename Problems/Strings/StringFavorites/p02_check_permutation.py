# O(N)
import unittest
from collections import Counter

"""
Intuition:
    - NOTE: Permutation: 1. MUST be same length   2. Same string when sorted
    - Sort both strings
    - Iterate over both strings from start, if there is mismatch, it is NOT permutation
Time: O(n log n) sort
Space: O(1) if we do in place and change input
# """
def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1) - 1):
        if s1[i] != s2[i]:
            return False
    return True

"""
Intuition:
    NOTE: 
        We allow all ASCII characters
        What is a Permutation:    1. Same length        2. Same counts of each character
    - Count the occurances of each character
    - Create a character to count map using an Array. Indices are ascii values, values are counts
    - Walk through string 1. Convert char to ASCII value, increment count
    - Walk through string 2. Convert char to ASCII value, decrement count
        - IF the count is 0, that means our char is unique OR we have too many of it. return FALSE
"""
def check_permutation_by_count(str1, str2):
    # must be same length
    if len(str1) != len(str2):
        return False
    counter_1 = [0] * 256
    counter_2 = [0] * 256

    for c in str1:
        counter_1[ord(c)] += 1
    for c in str2:
        counter_2[ord(c)] += 1
        
    for a,b in zip(counter_1, counter_2):
        if a != b:
            return False
    return True


def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
