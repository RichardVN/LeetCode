"""
TODO: this is just a subset question with a specific Base case of when to append

N-Way Decision Tree:
    - We choose any available [1..N] candidates
    - Then we choose an available [2..N] candidates.. and so on

Time: O(K * N^k) ... N branches, choose k times   copy k size combo
Space: O(k) ... to maintain current combination

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # choose from candidates 1 to N
        def dfs(i):
            # Unlike subsets (append when out range), we append when we hit certain k length
            if len(combo) == k:
                combos.append(combo[:])
            # i is out of valid candidate range
            if i > n:
                return
            # decision tree
            combo.append(i)
            dfs(i+1)
            combo.pop()
            dfs(i+1)

        
        combo, combos = [],[]
        # first valid candidate is 1
        dfs(1)
        return combos

"""
Alternative Solution using For Loop
- append case:  we append only subsets at certain length
- TODO: for loop handles index bounds and SKIP Choice
"""        
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            # append case?
            if len(combo) == k:
                combos.append(combo[:])
                return
            # decision , bounded
            for j in range(i,n+1):
                combo.append(j)
                dfs(j+1)
                combo.pop()
            return

        combo , combos = [], []
        dfs(1)
        return combos