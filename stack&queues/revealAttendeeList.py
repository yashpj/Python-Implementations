from collections import deque

def rev(arr):

    n = len(arr)
    index_queue = deque(range(n))
    result = [0]*n

    for i in sorted(arr):
        result[index_queue.popleft()] = i
        if index_queue:
            index_queue.append(index_queue.popleft())

    return result

print(rev([17,13,11,2,3,5,7])) 
print(rev([1,1000]))  
print(rev([1,2,3,-1,-2]))