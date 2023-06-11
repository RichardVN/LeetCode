"""
Keep track of good nodes throughout tree -> global var

dfs : pass DOWN highest value seen so far in path.  Don't return anything up, void
    - if root.val more than value, increment good node count and replace highest
    - if more than value, only reset highest

problem / subproblem:  not really one .. just make sure call dfs(children, highest) to traverse

Time: O(N) to dfs
Space: O(N)
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # void func .. dont return anything up, just passing down highest
        def dfs(root, highest):
            nonlocal numGood
            if not root: return
            if root:
                if root.val >= highest:
                    numGood += 1
                    # update highest in both cases: good or bad node
                    highest = root.val
                # dfs into children, passing down highest in path from root
                dfs(root.left, highest)
                dfs(root.right, highest)
        
        numGood = 0
        dfs(root, -float("inf"))
        return numGood