"""
NOTE:  Reverse Polish Notation: we are only given integers and operators, NOT operators or full string expression
- iterate through tokens RPN.
    - push non-operators on stack
    - if encounter operator token ... pop() the necessary integers, perform operation, then push onto stack
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(a-b)
            elif c == "*":
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                # TODO: order matters for division!!  5 // -10  -> -.5 rounded down to -1
                stack.append(int(b/a))
            # c is an integer
            else:
                stack.append(int(c))
        return stack[0]