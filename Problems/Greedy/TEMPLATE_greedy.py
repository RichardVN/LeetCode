"""
We can use greedy if following conditions are satisfied
    1. We want to optimize something
    2. A decision we make will NOT affect future decision. (or else would be a DP problem with 'states')

Time: O(N)
Space: O(1)
"""

def greedy(a):
	for i in range(a):
		x = select(a)
		if feasible(x):
			solution = solution + x
	return solution

'select a candidate for the solution'
def select():
	pass

'If the selected solution is feasible, build it to the result. Reset'
def feasible():
	pass