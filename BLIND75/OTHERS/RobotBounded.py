"""
INTUITION:
    - If position has not changed, TRUE cycle
    - If position has changed:
        - If direction changes ANY direction TRUE cycle
        - direction same: NOT cycle
        
                                    1
Direction:    -1  x  1              y
                                    -1
                                    
position:  x, y
                        
    
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # what to increment x and y on go
        dirX = 0
        dirY  = 1
        
        x = 0
        y = 0
        
        # execute instructions
        for d in instructions:
            if d == "G":
                x += dirX
                y += dirY
            # swap x and y direction. pos Y turn left, now face negative x
            elif d == "L":
                dirX, dirY = -dirY, dirX
            else:
                dirX, dirY = dirY, -dirX
                
        # position not changed
        if x == 0 and y == 0:
            return True
        # position changed
        if dirX != 0 or dirY != 1:
            return True
        return False