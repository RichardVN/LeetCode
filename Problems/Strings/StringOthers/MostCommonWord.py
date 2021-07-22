"""
NOTE: to change character we have to conver to list
NOTE: to split words we have to convert to string
Approach:  Change punctuation to " ", split, count hash map
Time: O( N + M), N is characters in paragraph and M is char in banned
Space: O(N + M),  have to store freq of words and banned

"""

from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        word_count = defaultdict(int)
        
        # replace punctuation with whitespace so we can split
        punctuation = set("!?',;.'")
        chars = list(paragraph)
        for i, c in enumerate(chars):
            if c in punctuation:
                chars[i] = " "
        paragraph = "".join(chars)
        # split by whitespace and lower
        words = paragraph.lower().split()
        for word in words:
            if word not in banned:
                word_count[word] += 1
        # return max word in word_count, with max being determined by KEY VALUE
        most_common = max(word_count, key=lambda k:word_count[k])
        return most_common