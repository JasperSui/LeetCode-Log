class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            if not self.is_valid(row): return False
        
        for col in zip(*board):
            if not self.is_valid(col): return False
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                unit_list = [board[a][b] for a in range(i, i+3) for b in range(j, j+3)]
                if not self.is_valid(unit_list): return False
        return True
        
        
    def is_valid(self, unit_list):
        unit_list = [unit for unit in unit_list if unit != "."]
        return len(set(unit_list)) == len(unit_list)        
        
        
        
#         for i in range(9):
#             temp = [1] * 10
#             for j in range(9):
#                 if board[i][j] == ".": continue
#                 index = int(board[i][j])
#                 if temp[index] > 0: temp[index]*= -1
#                 else: return False
        
#         for i in range(9):
#             temp = [1] * 10
#             for j in range(9):
#                 if board[j][i] == ".": continue
#                 index = int(board[j][i])
#                 if temp[index] > 0: temp[index] *= -1
#                 else: return False
        
#         a = [[0,1,2],[3,4,5], [6,7,8]]
#         b = [[0,1,2],[3,4,5], [6,7,8]]
#         for temp_a in a:
#             for i in temp_a:
#                 temp = [1] * 10
#                 for temp_b in b:
#                     for j in temp_b:
#                         if board[i][j] == ".": continue
#                         index = int(board[i][j])
#                         if temp[index] > 0: temp[index] *= -1
#                         else: return False
        
#         return True
                