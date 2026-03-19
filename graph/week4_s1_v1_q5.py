import heapq
def organize_fabrics(fabrics):
    max_heap = []
    for (i,j) in fabrics: # O(n)
        heapq.heappush(max_heap, (-1*j, i)) # O(log n)
    
    result = []
    while max_heap:
        value, brand = heapq.heappop(max_heap)
        result.append(brand)
    return result

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

'''fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]


stack1 = [6,7,8]
stack2 = []
'''
