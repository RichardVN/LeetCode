"""
Generate the different ways we can partitions of a string, such that part1 + part2 + ... == s

dfs(i)  where i indicates the position of string slice s[i:]

For any decision, we take all possible slices s[j:]

Time: 2^N , where N is length of string
"""
def generatePartitions(s):
    def dfs(i):
        if i== len(s):
            partitions.append(partition.copy())
            return
        # For this given slice s[i:], take every possible slice from i to end
        for j in range(i, len(s)):
            # INCLUSIVE!
            partition.append(s[i:j+1])
            dfs(j+1)
            partition.pop()


    partitions = []
    partition = []
    dfs(0)

    return partitions
res = generatePartitions("abc")
print(res)