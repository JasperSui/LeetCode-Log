class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    flag = 1
                    if i > 0 and board[i-1][j] == "X":
                        flag = 0
                    if j > 0 and board[i][j-1] == "X":
                        flag = 0
                    ans += flag
        return ans