
def check_stock(inventory, part_id):
    
    def recurse(low,high, inventory, part_id):
        mid = low + (high-low)//2
        
        if inventory[mid] == part_id:
            return True
        
        if low>high:
            return False
        
        if inventory[mid]>part_id:
            return recurse(low,mid - 1, inventory, part_id)
        else:
            return recurse(mid + 1,high, inventory, part_id)
    
    return recurse(0, len(inventory)-1, inventory, part_id)

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))


