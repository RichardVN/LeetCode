"""
Key Notes:
- hash map of CLOSE to OPEN
- stack. only append Open brackets to stack ... pending to be closed
- if encounter close brace, use map to check if it matches stack[-1]
- valid if end up with empty stack

Time: O(N)  to iterate through each character in the string
Space: O(1) the hash map is constant space and does not depend on size of string
"""
class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        brackets = []
        for c in s:
            # append ONLY open brackets to stack .. pending close
            if c in close_to_open.values():
                brackets.append(c)
            # closing bracket. Pop IF brackets not empty and ensure match to last open bracket
            elif c in close_to_open:
                if not brackets or close_to_open[c] != brackets.pop():
                    return False
        # TODO: at end of string, stack should be resolved / empty
        return not brackets