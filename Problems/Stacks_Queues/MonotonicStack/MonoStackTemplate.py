"""
TEMPLATE: 
- the stack contains array indices, not array items themselves
- For loop to iterate thru array
    - inner While loop to POP on a CONDITION (stackTop ? Array[i])
    - We only enter while loop on 2nd iteration ... check if stack exists

- "NEXT":  we process poppedTop in while loop
- "PREVIOUS":  we process stackTop AFTER while loop  ... we have to use STRICT operator
- At end of for loop we push i to stack
"""
def nextGreater():
    stack = []
    # result array that we update when we process in 2a or 2b
    nextGreater = [-1] * len(nums)

    for i, num in enumerate(nums):
        # TODO: 1. Loop to POP while we have found Condition for stackTop and Num
        while stack and num > stack[-1][1]:    # num  `COMPARATOR`  stackTopELEMENT
            # if pending condition satisfied, we pop
            poppedi, poppedNum = stack.pop()

            # TODO: 2a. process poppedTop?  ... NEXT
            nextGreater[poppedi] = num

        # TODO: 2b. do something with remaining stackTop after pops?   ... PREVIOUS   (we popped until we hit previous greater)
        if stack:
            #  previousGreater[i] = stack[-1]
            pass
        
        # TODO: 3. push the current INDEX on to stack
        stack.append(i,num)
