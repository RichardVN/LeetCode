"""
Variables to store info as we parse

Res:  holds result of 'subproblem' ... resets on new OPEN paranthesis
Curr: holds integer of consecutive digits ... resets on ANY non-digit char
Sign:  signals we process curr to res.  Update sign +1 or -1


Stack: [] push res, sign on (  .... pop sign, res on )

TIME: O(N)
SPACE: O(N)
"""

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        
        curr = 0
        sign = 1
        stack = [] # stack of RES for each 'subproblem'

        for c in s:
            # digit -- this is the only branch we update curr and not res
            if c.isdigit():
                curr = curr * 10 + int(c)

            # sign - breakpoint,  have to process curr to res. Reset curr
            elif c in ["+","-"]:
                res += sign * curr
                sign = -1 if c == "-" else 1
                
                curr = 0

            # open paranthesis - have to save our curr and sign to stack
            # this is as if we are opening another subproblem from scratch. reset res!
            elif c == "(":
                stack.append(res)
                stack.append(sign)

                curr = 0
                res = 0
                sign = 1

            # close paranthesis -  breakpoint, update this res, and cumulate w/ prev res. Reset curr
            elif c == ")":
                res += sign * curr # Add whatever is just before paranthesis
                res *= stack.pop() # apply the sign to this subproblem res
                res += stack.pop() # retrieve previous stored res and join
                
                curr = 0

            # whitespace


        return res + sign * curr # TODO: remaining digit at end since no operand at end