'''
You are an architect tasked with designing a dream building layout. 
The building layout is represented by a string s of even length n. 
The string consists of exactly n / 2 left walls '[' and n / 2 right walls ']'.

A layout is considered balanced if and only if:

It is an empty space, or
It can be divided into two separate balanced layouts, or
It can be surrounded by left and right walls that balance each other out.
You may swap the positions of any two walls any number of times.

Return the minimum number of swaps needed to make the building layout balanced.

][][

]]][[[

[][][][]

stack = ('[')
Just wanted to clarify that ceiling question, the ceiling is for cases where the number of swaps needed is odd.
We need to use integer by 2 division (because we cannot have .5 swaps), 
so in the odd case we need to round up -> ceiling.
'''

def min_swaps(s):
    imbalance = 0
    max_imbalance = 0
    
    for wall in s:
        if wall == '[':
            imbalance -= 1
        else:
            imbalance += 1
            
        max_imbalance = max(max_imbalance, imbalance)
            
    return (max_imbalance + 1) // 2


print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  

