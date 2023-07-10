# 3.4 Queue Via Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
"""
Intuition:
    - Implement queue via two stacks
    - Stack_new has newest values on top
        - Every time we push(), we push to stack_new
    - Stack_old has oldest values on top
        - Every time we pop() or peek(), we pop / peek from stack_old
        - TODO: If the stack_old is empty, Pop from stack_new until empty and push on stack_old
"""
class MyQueue:

    def __init__(self):
        self.qback = []
        self.qfront = []
        

    def push(self, x: int) -> None:
        self.qback.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.qfront:
            while self.qback:
                val = self.qback.pop()
                self.qfront.append(val)

        return self.qfront.pop()
        

    def peek(self) -> int:
        if self.empty():
            return None
        if not self.qfront:
            while self.qback:
                val = self.qback.pop()
                self.qfront.append(val)
        return self.qfront[-1]
        

    def empty(self) -> bool:
        return not(self.qback or self.qfront)