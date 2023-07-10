"""
find NEXT warmer --> monotonic decreasing stack

stack:
    - push items that are pending finding nextWarmer
    - While (found nextWarmer:
        pop() and update result array

Time: O(N)
Space: O(N)

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # finding the NEXT warmer temp  -> implies monotonic stack

        # res will be index Difference
        res = [0] * len(temperatures)

        # stack for items pending Next Warmer
        s = []

        for i, temp in enumerate(temperatures):
            # while:  if we found next warmest
            while s and temp > s[-1][1]:
                # we found nextWarmer for this popped item
                poppedi, poppedTemp = s.pop()
                daysWait = i - poppedi
                res[poppedi] = daysWait

            s.append( (i, temp) )
        return res