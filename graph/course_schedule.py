from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                count += 1
        
        if count == numCourses:
            return True

        return False
    
