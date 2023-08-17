# 542. 01 Matrix

# Medium

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		row, col = len(mat), len(mat[0])
		queue = deque([])

		for x in range(row):
			for y in range(col):
				if mat[x][y] == 0:
					queue.append((x, y, 1))


		return self.bfs(row, col, queue, mat)

	def bfs(self, row, col, queue, grid):
		visited = set()
		while queue:
			x, y, steps = queue.popleft()

			for nx, ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
				if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
					if grid[nx][ny] == 1:
						visited.add((nx,ny))
						grid[nx][ny] = steps
						queue.append((nx, ny, steps+1))

		return grid
	
# time complexity: O(mn)
# space complexity: O(mn)