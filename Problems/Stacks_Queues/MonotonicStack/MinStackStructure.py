"""
Two Stacks:
    - all_stack with all pushed values
    - min_stack that contains the "minimums" such that the min vals are decreasing from left to right

When Pushing:  push onto min_stack even if the value is EQUAL to current minimum
When Popping:  only pop from min_stack if the value matches the popped from all_stack

TIME: O(1) for all operations
SPACE: O(2N)

"""

class MinStack:

    def __init__(self):
        self.all_stack = []
        # whenever push to all_stack, maintain current minimum and push it to min_stack
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.all_stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            val = self.min_stack[-1]
        self.min_stack.append(val)

    def pop(self) -> None:
        self.all_stack.pop()
        self.min_stack.pop()        
        

    def top(self) -> int:
        return self.all_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
