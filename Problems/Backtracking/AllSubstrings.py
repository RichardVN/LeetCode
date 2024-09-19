def generateSubstrings(s):
    substring, substrings = [], []

    for i in range(0, len(s)):
        for j in range(i, len(s)):
            substrings.append(s[i : j+1])

    return substrings

res = generateSubstrings("aabbbc")
print(res)