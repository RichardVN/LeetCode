"""
Path Problems vs Backtrack:
TODO: Typically, DP will be applicable when the allowed movement is constrained in a way that prevents moving "backwards", for example if we are only allowed to move down and right.


State Variables:
    - r, c, someConstraint
    
Recursive Relation:
    - Usually related to traversal options ... 
    - Subproblems are the possible cells we can choose to move to
        e.g. if you can only go right and down:  dp(r,c) =  SOLVE_USING_SUBPROBLEMS( dp(r + 1, c) , dp(r, c + 1 ))

"""