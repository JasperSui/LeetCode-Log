class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            for i in graph[cur]:
                dfs(i, path + [i])
        dfs(0, [0])
        return res