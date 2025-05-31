class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.nrow = len(board)
        goal = self.nrow * self.nrow
        
        queue = [(1, 0)]
        visited = set()
        
        while queue:       
            cur, step = queue.pop(0)
            if cur == goal:
                return step
            
            for move in range(1, 7):
                ncell = cur + move          
                if ncell > goal:
                    break
                r, c = self.n2rc(ncell)
                if (r, c) not in visited:
                    visited.add((r, c))
                    if board[r][c] != -1:
                        ncell = board[r][c]
                    queue.append((ncell, step + 1))
        
        return -1
                        
                        
    def n2rc(self, n):        
        row = (n - 1) // self.nrow
        row = self.nrow - row - 1
        
        col = (n - 1) % self.nrow
        if (self.nrow - row) % 2 == 0:
            col = self.nrow - col - 1
        return row, col

# 2 Approach
    
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]
        for i in range(n):
            if i % 2 == 0:
                arr += board[n - i - 1]
            else:
                arr += board[n - i - 1][::-1]
        dist = [-1] * len(arr)
        dist[1] = 0
        q = deque([1])
        while q:
            square = q.popleft()
            l = square + 1
            r = min(square + 6, n**2)
            for i in range(l, r + 1):
                next_square = i if arr[i] == -1 else arr[i]
                if dist[next_square] == -1:
                    dist[next_square] = dist[square] + 1
                    q.append(next_square)
        return dist[n * n]