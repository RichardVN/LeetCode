"""
"Find the minimal k , such that condition(k) is True"


Map sorted array into True or False based on condition

Sorted Array: [ a, b, c, d, e]
Condition?  : [ F, F, F, T, T]
                         L
                         ^ After while loop, L will be the first k that satisfies condition.
                            
1. Initialize the boundary variables left and right to specify search space. Include ALL possible elements;
2. Decide return value. Is it return left or return left - 1? TODO: Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min('search_space'), max('search_space') # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid     # Try to find an earlier True
        else:
            left = mid + 1
    return left


"""
Single Unique Target:  Classic Binary Search
"""
def bs(nums, l, r, target):
    while l <= r:
        m = (l+r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m -1
        else:
            # TODO: found target, no need to look any further
            return m
    return -1

"""
Duplicate targets: Left-Biased Binary Search

' Find the leftmost instance of our target value '
T t t t
"""
def bs_left(nums, l, r, target):
    res = -1
    while l <= r:
        m = (l+r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m -1
        else:
            # TODO: found target, but look left for smaller
            res = m
            r = m - 1
    return res


"""
Duplicate targets: Right-Biased Binary Search

' Find the rightmost instance of our target value '
t t t T
"""
def bs_right(nums, l, r, target):
    while l <= r:
        m = (l+r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m -1
        else:
            # TODO: found target, but look right for greater
            res = m
            l = m + 1
    return res

"""
Minimal fulfilled condition

' Find the minimal k , such that condition(k) is True '
f f f T t t
"""
def bs_minimal(nums, l, r, target):
    while l <= r:
        k = l + (r-l)// 2
        if isCondition(k):
            r = k - 1   # see if we can achieve with smaller k, LEFT-biased
        else:
            l = k + 1
    return l

"""
Maximal fulfilled condition

' Find the maximal k , such that condition(k) is True '
t t T f f f
"""
def bs_minimal(nums, l, r, target):
    while l <= r:
        k = l + (r-l)// 2
        if isCondition(k):
            l = k + 1   # see if we can achieve with larger k, RIGHT-biased
        else:
            r = k - 1
    return r


# Test cases
b = [0, 10, 10, 30]

l = 0
r = len(b) - 1
t = 10
res = bs_left(b, l, r, t)

print(res)