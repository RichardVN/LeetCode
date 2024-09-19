class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = []
        
        for i, num in enumerate(nums):
            idxMark = abs(num) - 1
            if nums[idxMark] < 0:
                dupes.append(abs(num))
            else:
                nums[idxMark] = -1 * nums[idxMark]
        
        return dupes