# 1496. Path Crossing

# Easy

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise. 

# Example 1:

# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
 

# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        keyx,keyy = 0,0
        cor = {(keyx,keyy): 1}
        for i in path:
            if i == "N":
                keyy += 1
            elif i == "E":
                keyx += 1
            elif i == "S":
                keyy -= 1
            elif i == "W":
                keyx -= 1
            
            if (keyx,keyy) in cor:
                return True
            else:
                cor[(keyx,keyy)] = 1
        return False