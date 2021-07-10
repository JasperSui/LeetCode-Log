class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            temp_res = res.copy()
            temp_res.append(1)
            for j in range(1, len(temp_res)-1):
                temp_res[j] = res[j] + res[j-1]
            res = temp_res
        return res