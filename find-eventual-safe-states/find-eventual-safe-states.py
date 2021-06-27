class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        innode = defaultdict(list)
        queue = []
        for i in range(n):
            outdegree[i] = len(graph[i])
            if outdegree[i] == 0: queue.append(i)
            for j in graph[i]:
                innode[j].append(i)
        
        for term_node in queue:
            for in_node in innode[term_node]:
                outdegree[in_node] -= 1
                if outdegree[in_node] == 0:
                    queue.append(in_node)
        return sorted(queue)