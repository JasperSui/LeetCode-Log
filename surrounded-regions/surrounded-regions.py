class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Check border
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(board, i, 0, m, n)
            if board[i][n-1] == "O":
                self.dfs(board, i, n-1, m, n)
        
        # Check border
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(board, 0, j, m, n)
            if board[m-1][j] == "O":
                self.dfs(board, m-1, j, m, n)
        
        # Iterate it
        for i in range(m):
            for j in range(n):
                char = ""
                if board[i][j] == "O":
                    char = "X"
                if board[i][j] == "#":
                    char = "O"
                if char:
                    board[i][j] = char
        
    def dfs(self, board, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != "O": return
        board[i][j] = "#"
        self.dfs(board, i+1, j, m, n)
        self.dfs(board, i-1, j, m, n)
        self.dfs(board, i, j+1, m, n)
        self.dfs(board, i, j-1, m, n)