"""
https://leetcode.com/problems/longest-palindromic-substring/submissions/
2 cases of palindromes:
    Odd: there is one middle. That may not have matching char, aka. odd parity
    Even: there are two middles. Each char has matching, even parity

        
Approach:
- create a method that expands from center / centers, and returns longest palindrome found
- loop through original string, call method twice for the two centers
- if we find a new longest palindrome:
    - update start and end of current longest palindrome so we can return the actual string
    
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPali(l, r):
            longest = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = r-l+1
                l -= 1
                r += 1
            # reached end
            return longest

        resStart = 0
        resEnd = 0
        for i in range(0, len(s)):
            thisLongest = max(longestPali(i,i), longestPali(i, i+1))
            # update longest marker, if new best
            if thisLongest > resEnd - resStart + 1:
                # longest can be odd  "aba"
                if thisLongest % 2 != 0:
                    resStart = i - thisLongest // 2
                    resEnd = i + thisLongest // 2
                # or even "abba"
                else:
                    resStart = i - thisLongest // 2 + 1
                    resEnd = i + thisLongest // 2
        
        return s[resStart : resEnd + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start = 0
        end = 0
        
        # check all centers
        for i in range(len(s)):
            # case 1 middle:
            longest_one_center = self.expand_from_center(s, i, i)
            # case 2, two middles:
            longest_two_center = self.expand_from_center(s, i, i+1)
            # get longest palindrome between the two
            longest_total = max(longest_one_center, longest_two_center)
            
            # we have found new longest palindrome, move new start and end
            if longest_total > end-start: 
                start = i - (longest_total - 1) // 2        # -1 to handle even case length
                end = i + longest_total // 2
        
        # inclusive slice of end
        return s[start:end+1]
    
    # return int LENGTH longest palindrome of substring - O(N) time
    # if we handle TWO middle chars, right starts at left + 1
    def expand_from_center(self, s, left, right):
        if not s:
            return None

        # conditions for while loop to keep expanding:
        # 1. left is >= 0
        # 2. right is < length of string
        # 3. char at left and right are the same
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # valid palindrome, expand bounds. 
            left -= 1
            right += 1

        # invalid, return length of last valid (add 1 to left, remove 1 from right: R-1  -  L+1  +1 )
        # +1 because inclusive of both indices
        return right - left -1
    
    
class CleanSolution4:
    def longestPalindrome(self, s: str) -> str:
        if s is '': 
            return s
        max_len = 0 
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2
        return s[start:end+1]

    def expandFromCenter(self, s, idx1, idx2):
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
        return idx2 - idx1 - 1 
