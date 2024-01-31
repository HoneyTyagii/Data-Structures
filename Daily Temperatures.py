# 739. Daily Temperatures

# Medium

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead. 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
	    days_count = len(T)
	    next_warm_day = [0 for _ in range(days_count)]
	    for d in range(days_count - 2, -1, -1):
	    	next_day = 1
	    	while next_day and T[d + next_day] <= T[d]: 
	    		if next_warm_day[d + next_day]:
	    			next_day += next_warm_day[d + next_day]
	    		else:
	    			next_day = 0
	    	next_warm_day[d] = next_day
	    return next_warm_day