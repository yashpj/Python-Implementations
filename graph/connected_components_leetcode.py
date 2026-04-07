from collections import defaultdict, deque
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        graph = defaultdict(list)
        visited = [False for _ in range(n)]

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(i):

            queue = deque([i])
            
            while queue:
                x = queue.popleft()
                visited[x] = True
                for i in graph[x]:
                    if not visited[i]:
                        queue.append(i)
            

        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)
        return count
        
        