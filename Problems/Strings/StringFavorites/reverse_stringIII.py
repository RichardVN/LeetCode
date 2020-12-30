class Solution:
    def reverseWords(self, s: str) -> str:
        # break string into list of strings  O(N)
        words = s.split()
        # for each word string    O(N)
        for i in range(len(words)):
            # TODO: Instead of converting the word-string into a list of chars and reversing which takes O(s) space
                #   Just get a reverse sliced copy
            # 1. for each word string, break the string into a list of chars   O(s)
            word_chars = list(words[i])
            # 2. reverse the list of chars         O(s)
            word_chars.reverse()
            # 3. join the list of chars into a word-string    O(s)
            words[i] = ''.join(word_chars)
        # join the list of strs into a string    O(N)
        return " ".join((words))

    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)
