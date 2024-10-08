"""
See "AllSubstringPartitions"
Only append if we were able to rech end

TIME:  O(N * 2^N)  ... Combinations question. For each index, we decide to partition or not. 
SPACE: O(N)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i):
            # base
            if i >= len(s):
                partitions.append(partition[:])
                return

            # decisions
            for j in range(i, len(s)):
                # Check if it is valid palindrome before appending ... 
                # if not, we don't cut slice here AND we don't progress i towards len(s)
                if self.isPali(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
            return


        partitions, partition = [], []
        dfs(0)
        return partitions
    
    def isPali(self, s, l , r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
