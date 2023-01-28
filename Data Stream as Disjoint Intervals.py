# 352. Data Stream as Disjoint Intervals

# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

# Implement the SummaryRanges class:

# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

# Example 1:

# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

# Constraints:

# 0 <= value <= 104
# At most 3 * 104 calls will be made to addNum and getIntervals.

class SummaryRanges:

	def __init__(self):
		self.set = set()

	def addNum(self, value: int) -> None:
		self.set.add(value)

	def getIntervals(self) -> List[List[int]]:

		result = []
		index = 1
		array = sorted(list(self.set))
		
		start = array[0]
		current_element = array[0]

		if len(array) == 1:
			result.append([start, start])
			return result

		while index < len(array):

			if array[index] != current_element + 1:
				result.append([start, array[index - 1]])
				start = array[index]

			current_element = array[index]
			index = index + 1

		result.append([start,array[index - 1]])

		return result 
		