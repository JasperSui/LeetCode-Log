class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        
        # undirected graph
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        # eats leaves from outside circally
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        # There will be at most 2 nodes in the center
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                # Remove the connection between i and j
                # remove j from adj[i]
                j = adj[i].pop()
                
                # remove i from adj[j]
                adj[j].remove(i)
                
                # if only one node connects j, then j will be the new leave
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        
        # Return the rest of leaves, which means the most center node(s)
        return leaves