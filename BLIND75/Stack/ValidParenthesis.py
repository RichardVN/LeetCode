"""
Approach:  hash map {closing_brace : open_brace}, push open_brace on stack to be resolved

Intuition:
    - We know every time we encounter close brace, the MOST recent open brace should be same type
    - We want to query open brace type in O(1) with just close brace type
Time: O(N) to step thru string
Space: O(1) for constant space braces, O(N) for stack
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # once we reach close, wanna check corresponding open
        close_to_open = {
            ']':'[',
            ')':'(',
            '}':'{'
            
        }
        # stack of open paranthesis have to resolve
        stack = []
        
        open_brackets = "[({"
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            # we hit close bracket
            else:
                if not stack:
                    return False
                # compare if type closing matches type opening
                if close_to_open[bracket] != stack.pop():
                    return False
                # otherwise continue, and we already popped matching opening
        if stack:
            return False
        
        return True