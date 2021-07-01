class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if not self.is_valid(row):
                return False
        
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                units = [board[a][b] for a in range(i, i+3) for b in range(j, j+3)]
                if not self.is_valid(units):
                    return False
        return True
        
    
    def is_valid(self, units):
        units = [u for u in units if u != "."]
        return len(units) == len(set(units))