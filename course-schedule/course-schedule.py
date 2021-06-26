class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # -1: being visited, 0: not visited before, 1: have been visited
        
        # You are visiting a node which is "being visited", so there is a CYCLE HERE
        # Remember topological sort is must be a DAG (Direct Acyclic Graph)
        if visited[i] == -1:
            return False
        
        # if the node is visited already, then pass it.
        if visited[i] == 1:
            return True
        
        # Because you are ready to visit other nodes, mark the current node as -1 for being visited.
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        
        visited[i] = 1
        return True