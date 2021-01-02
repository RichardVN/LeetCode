"""
Intuition:
    - Create a hash map that associates closing brace with open brace
    - Iterate through the string
        - Every time we meet a open bracket, pop onto stack
        - Every time we meet closing bracket, pop whatever on the stack
            - Check to see if stack is empty
            - Check that the open brace associated w/ closing brace (from hash map) is the same char we popped off
    - Return true if the stack is empty

Time: O(N)  to iterate through each character in the string
Space: O(1) the hash map is constant space and does not depend on size of string
"""
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