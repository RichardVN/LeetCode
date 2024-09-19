"""
For usage when you have numbers in range [1, 2, 3 ... N]

For a value num, its proper sorted index is at num - 1
    - indices go [0, 1, ..., N-1]

    0   1  2
    [3, 1, 2]
    i
"""


def cycleSort(nums):
    i = 0

    # inc i only if num is at correct index
    while i < len(nums):
        correctIndex = nums[i] - 1
        if i == correctIndex:
            i += 1
        else: 
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]

    return nums

cases = [
    [3, 1, 2],
    [7,6,3,4,5,2,1]

]
for case in cases:
    print(cycleSort(case))