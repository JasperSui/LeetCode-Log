"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        def dfs(_node, m):
            for neigh in _node.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                    dfs(neigh, m)
                m[_node].neighbors.append(m[neigh])
        m = {node: Node(node.val)}
        dfs(node, m)
        return m[node]
        
        
        # # DFS (recursive)
        # if not node: return
        # def dfs(_node, m):
        #     for neigh in _node.neighbors:
        #         if neigh not in m:
        #             m[neigh] = Node(neigh.val)
        #             dfs(neigh, m)
        #         m[_node].neighbors.append(m[neigh])
        # m = {node: Node(node.val)}
        # dfs(node, m)
        # return m[node]
        
        
        
        # # BFS
        # if not node: return
        # m = {node: Node(node.val)}
        # queue = deque([node])
        # while queue:
        #     n = queue.popleft()
        #     for neigh in n.neighbors:
        #         if neigh not in m:
        #             # Append the node should be traverse soon
        #             queue.append(neigh)
        #             m[neigh] = Node(neigh.val)
        #         m[n].neighbors.append(m[neigh])
        # return m[node]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # DFS
        # if not node: return
        # # m[node] == cloned graph
        # m = {node: Node(node.val)}
        # stack = [node]
        # while stack:
        #     n = stack.pop()
        #     for neigh in n.neighbors:
        #         if neigh not in m:
        #             stack.append(neigh)
        #             m[neigh] = Node(neigh.val)
        #         m[n].neighbors.append(m[neigh])
        # return m[node]