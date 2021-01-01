class Solution:
    def isValid(self, s: str) -> bool:
        # dict to lookup corresponding closing paranthesis
        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        parenthesis_stack = []
        
        for char in s:
            if char in close_to_open.values():
                parenthesis_stack.append(char)
            elif char in close_to_open:
                if not parenthesis_stack:
                    return False
                if close_to_open[char] != parenthesis_stack.pop():
                    return False
        return not parenthesis_stack