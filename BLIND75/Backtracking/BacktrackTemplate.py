"""
Goal:
    - Generate all possible subsets given N elements
    - Find set of all subsets of set S (given elements)

At each step:
    - Include element in subset, or exclude element from subset
    - Choice made for all N elements
        --> O(N  *  2^N)
    - KEY:  dfs traversal undoes previous decisions by removing previous choice 
            from current subset
"""

class Solution: 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.dfs(0, res, path, nums)
        return res

    def dfs(self, index, res, path, nums):
        res.append(list(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(i + 1, res, path, nums)
            path.pop()
