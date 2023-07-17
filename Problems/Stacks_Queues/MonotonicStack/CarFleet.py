"""
clump to fleet if a behind_car has faster finish time than ahead_car
-> must SORT by position

Maintain a stack of strictly increasing fleet times. 
- only append a time if it is greater than time at top of stack

TIME: O(N LOG N)
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack of fleet times... mono strictly increasing fleet times .. pending next ~smaller
        s = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            distance_left = target - pos
            time = distance_left / spd
            if not s or time > s[-1]:
                # has smaller time than previous fleet. Clump and dont add to stack
                s.append(time)
        # return stack, which is a list of unique fleet times
        return len(s)


"""
Stackless Solution.  
    - sort cars by position
    - calculate time_to_target for each car
    - `last_fleet_time` to maintain time previous fleet
    - `fleets` counter. Increment ONLY if we found a time greater than previous fleet
"""
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        last_fleet_time = -1

        for pos, spd in sorted(zip(position, speed), reverse=True):
            distance_left = target - pos
            time = distance_left / spd

            # we only increment fleet if time is larger
            # otherwise, the car would have caught up to previous and clumped
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time  # new fleet, new last_fleet_time

        return fleets