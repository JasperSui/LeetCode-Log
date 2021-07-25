class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        used = [0] * 8
        self.ans = 0
        m, n = len(students), len(students[0])
        self.dfs(students, mentors, 0, 0, m, n, used)
        return self.ans
    
    def dfs(self, students, mentors, i, score, m, n, used):
        if i == m:
            self.ans = max(self.ans, score)
            return
        for j in range(m):
            if used[j]:
                continue
            used[j] = 1
            s = 0
            for k in range(n):
                if students[i][k] == mentors[j][k]:
                    s += 1
            self.dfs(students, mentors, i+1, score+s, m, n, used)
            used[j] = 0
        