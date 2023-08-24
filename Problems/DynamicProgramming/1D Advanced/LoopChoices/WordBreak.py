from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return True
            # does beginning start with any dict words?
            for word in wordDict:
                if s[i: i + len(word)] == word:
                    res = dfs(i + len(word))
                    # TODO: if we have found one path to break to end of s, we can stop here
                    if res:
                        return True
            return False
        return dfs(0)