class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        row_s, row_e, col_s, col_e = 0, n-1, 0, n-1
        count = 1
        while row_s <= row_e and col_s <= col_e:
            for i in range(col_s, col_e+1):
                res[row_s][i] = count
                count += 1
            row_s += 1
            
            for i in range(row_s, row_e+1):
                res[i][col_e] = count
                count += 1
            col_e -= 1
            
            if row_s <= row_e:
                for i in range(col_e, col_s-1, -1):
                    res[row_e][i] = count
                    count += 1
            row_e -= 1
            
            if col_s <= col_e:
                for i in range(row_e, row_s-1, -1):
                    res[i][col_s] = count
                    count += 1
            col_s += 1
        return res