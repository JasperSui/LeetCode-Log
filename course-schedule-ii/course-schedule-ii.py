class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            indegree[x].add(y)
            outdegree[y].append(x)
        
        res, start = [], [i for i in range(numCourses) if not indegree[i]]
        while start:
            new_start = []
            for i in start:
                res.append(i)
                for j in outdegree[i]:
                    indegree[j].remove(i)
                    if not indegree[j]:
                        new_start.append(j)
            start = new_start
        return res if len(res) == numCourses else []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         indegree = [set() for _ in range(numCourses)]
#         outdegree = [[] for _ in range(numCourses)]
#         for course, pre in prerequisites:
#             indegree[course].add(pre)
#             outdegree[pre].append(course)
        
#         # start are all nodes without any prerequisites
#         res, start = [], [i for i in range(numCourses) if not indegree[i]]
        
#         while start:
#             new_start = []
#             for i in start:
#                 # append the course first
#                 res.append(i)
                
#                 # start to traverse the current courses' outdegree
#                 for j in outdegree[i]:
#                     indegree[j].remove(i)
                    
#                     # Append j to new start because there is no prerequisite anymore
#                     if not indegree[j]:
#                         new_start.append(j)
#             start = new_start
#         return res if len(res) == numCourses else []