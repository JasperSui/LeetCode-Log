class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        J = {i: None for i in list(J)}
        for i in list(S):
            if i in J: num += 1
        return num