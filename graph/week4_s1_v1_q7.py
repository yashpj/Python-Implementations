
def calculate_fabric_waste(items, fabric_rolls):
    total = 0
    print(fabric_rolls)
    for i in range(len(items)):
        total += fabric_rolls[i] - items[i][1]
    return total
    

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls3= [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls1))
print(calculate_fabric_waste(items_2, fabric_rolls2))
print(calculate_fabric_waste(items_3, fabric_rolls3))
