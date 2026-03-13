'''
You are given an array floors representing the heights of different building floors. Your task is to design a skyscraper using these floors, where each floor must be placed on top of a floor with equal or greater height. However, you can only start a new skyscraper when necessary, meaning when no more floors can be added to the current skyscraper according to the rules.

Return the number of skyscrapers you can build using the given floors.


understand:
[10, 5, 8, 3, 7, 2, 9]
[10,5]->
[8,3]
[7,2]
[9]
'''

def build_skyscrapers(floors):

    if len(floors) ==0:
        return 0
    count = 1
    
    for i in range(1,len(floors)):
        if floors[i-1]>=floors[i]:
            continue
        else:
            count += 1
    return count


print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
print(build_skyscrapers([10, 5, 8, 3, 4, 7, 2]))