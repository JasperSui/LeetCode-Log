class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = [0] * 101
        for birth, death in logs:
            l[birth-1950] += 1
            l[death-1950] -= 1
        max_num, max_year = l[0], 1950
        for i in range(1, len(l)):
            l[i] += l[i-1]
            if l[i] > max_num:
                max_num = l[i]
                max_year = i+1950
        return max_year