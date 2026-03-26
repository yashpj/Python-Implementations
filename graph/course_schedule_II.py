class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = { i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        while len(queue)>0:
            x = queue.popleft()
            result.append(x)
            for i in graph[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return result if len(result) == numCourses else []
                
## only visiting an edge inside the while loop only once. so tc is O(V+E)