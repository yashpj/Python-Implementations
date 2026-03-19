'''You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. 
Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics whose combined cost is the highest possible without exceeding the budget.

Write the find_best_fabric_pair() function, which takes a list of fabrics (each with a name and cost) and a budget. 
The function should return the names of the two fabrics whose combined cost is the closest to the budget without exceeding it.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 11), ("Hemp", 35)


[("Organic Cotton", 30),]

min_difference_till_now = 4
pair = ("Organic Cotton", "Hemp")


'''

def find_best_fabric_pair(fabrics, budget):
    min_difference_till_now = budget
    pair = []

    for i in range(0, len(fabrics)):
        for j in range(i+1,len(fabrics)):
            sum =  fabrics[i][1] + fabrics[j][1]
            if sum <=budget and (budget-sum)<min_difference_till_now:
                min_difference_till_now = budget - sum
                pair = [fabrics[i][0] , fabrics[j][0]]
    return pair


fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 11), ("Hemp", 35)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

