"""
Base Case:  Smallest subproblem. Usually relating to SIZE of input (unlike DP which is some base i)
    - RETURN up an answer that can be used by bigger problems

Recursive Case:  
    - typically DIVIDE input and pass to subproblem. (unlike DP which usually looks at i-1)
    - we COMBINE all the subproblem answers to determine answer to problem
        (NOTE: subproblem inputs together should equal THIS problem input)

"""

# def divide_and_conquer( S ):
#     # (1). Divide the problem into a set of subproblems.
#     [S1, S2, ... Sn] = divide(S)

#     # (2). Solve the subproblem recursively,
#     #   obtain the results of subproblems as [R1, R2... Rn].
#     results = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
#     [R1, R2,... Rn] = results

#     # (3). combine the results from the subproblems.
#     #   and return the combined result.
#     return combine([R1, R2,... Rn])