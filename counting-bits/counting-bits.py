class Solution:
    def countBits(self, num: int) -> List[int]:
        # res = [0]
        # while len(res) <= num:
        #     print(res)
        #     res += [i+1 for i in res]
        # return res[:num+1]
        
        # res = [0] * (num + 1) 
        # for i in range(1, num+1):
        #     res[i] = res[i//2] + i % 2
        # return res
        
        res = [0] * (num+1)
        offset = 1
        for i in range(1, num+1):
            if offset * 2 == i: offset *= 2
            res[i] = res[i - offset] + 1
        return res
        