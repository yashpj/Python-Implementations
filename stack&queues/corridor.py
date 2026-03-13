'''
You are an architect designing a corridor for a futuristic dream space. 
The corridor is represented by a list of integer values where each value represents the width of a segment of the corridor. 
Your goal is to find two segments such that the corridor formed between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.

area = min(1,6)*(2-0) = 12


'''

def max_corridor_area(segments):
    
    left = 0
    right = len(segments)-1
    area = 0

    while left < right:
        ar = min(segments[left],segments[right]) * (right - left)
        area = max(ar,area)

        if segments[left]< segments[right]:
            left += 1
        else:
            right -= 1
    return area


print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 
