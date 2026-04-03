import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacency_list = defaultdict(list)

        for x,y,w in times:
            adjacency_list[x].append((w,y))
        
        min_heap = []
        visited = [False for _ in range(n+1)]

        heapq.heappush(min_heap,(0,k))
        
        maxTime = 0
        while len(min_heap) > 0:
            travel_time, node = heapq.heappop(min_heap)

            if visited[node]:
                continue
            maxTime = travel_time

            visited[node] = True

            for time, vertex in adjacency_list[node]:
                if not visited[vertex]:
                    heapq.heappush(min_heap,(travel_time + time, vertex))
        
        for i in range(1,n+1):
            if not visited[i]:
                return -1
        return maxTime


