class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)
        d = defaultdict(list)
        
        # 想像以 mat[0][0], mat[1][1] 為基準點， 每一條線的左右每個點距離都是一樣的
        # 像是 mat[0][1] 距離 mat[0][0] 是 1, mat[1][2] 距離 mat[1][1] 也是 1
        # 所以他們會落在同一個 d[距離差] 裡
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i-j].pop()
        return mat