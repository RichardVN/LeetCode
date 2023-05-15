# https://leetcode.com/problems/top-k-frequent-elements/description/

"""
If we made a dict and tried to get k most freq, it would be k*N. We would
have to go through entire, unordered dict.

Method 1 - Bucket sort algorithm:
    - Hash Map of   num : counts
    - LIST... Indices (frequency)  -> Values (List of corresponding vals)
        - We know the list indices is bounded by N 
        - Worst case: all vals are put into bucket at index [1], O(N+N)
    - iterate through list in reverse, append vals from bucket to top_k result list.

Time: O(N+N)  ... iterate thru list, iterate thru buckets
Space: O(N)   ... space for hash map, freqs array
"""


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # N empty buckets ... [ [], [], [] ]. +1 b/c at most we can have freq of N
        freqs = [[] for _ in range(len(nums) + 1)]
        # hash map to get counts
        counts = dict()
        for num in nums:
            # if first time encounter key, set 0 first
            counts[num] = counts.get(num, 0) + 1

        # for each num in counts dict ... append to bucket at proper freq
        for num, count in counts.items():
            freqs[count].append(num)

        top_k = []
        # iterate in reverse  (start, end, step)
        for i in range(len(freqs) -1, -1 , -1):
            bucket = freqs[i]
            for n in bucket:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
        return None

        
        
        


"""
Method 2 - Using Counter class
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        most_common_pairs =  freqs.most_common(k)  # returns list of (key, Value) tuples

        return [pair[0] for pair in most_common_pairs] # we just want list of keys / nums

