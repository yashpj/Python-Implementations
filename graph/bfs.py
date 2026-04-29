
from collections import deque

def get_all_destinations(flights, start):
    result = set()
    visited = set([])
    
    queue = deque([])
    queue.append(start)
    
    while queue:
        city = queue.popleft()
        
        if city in visited:
            continue
            
        visited.add(city)
        result.add(city)
        
        for i in flights[city]:
            if i not in visited:
                queue.append(i)
    return list(result)
        
    


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))


