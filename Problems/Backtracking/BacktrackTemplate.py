class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs( index):
            res.append(list(decisions)) 
            for i in range(index, len(nums)):
                decisions.append(nums[i])
                dfs(i+1)
                decisions.pop()

        res, decisions = [], []
        dfs(0)
        return res
