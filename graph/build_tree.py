from collections import deque 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root




def search(inventory, name):
    if not inventory:
        return (False,None)
    if name == inventory.val:
        return (True,inventory)
    if name < inventory.val and inventory.left:
        return search(inventory.left, name)
    if name > inventory.val and inventory.right:
        return search(inventory.right, name)
    return (False,None)

def append(collection, name):
    if name < collection.val:
        if not collection.left:
            collection.left = TreeNode(name)
            return
        else:
            append(collection.left,name)
    else:
        if not collection.right:
            collection.right = TreeNode(name)
            return
        else:
            append(collection.right,name)


def add_plant(collection, name):
    #ifPresent,node = search(collection, name)
    #if not node:
    append(collection, name)
    #else:
        #append(node, name)
    return collection
        



"""

            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))



class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def evaluate(sign,val1,val2):
    if sign == "+":
        return val1 + val2
    if sign == "-":
        return val1 - val2
    if sign == "*":
        return val1 * val2

def calculate_yield(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return root.val
    
    x1 = calculate_yield(root.left)
    x2 = calculate_yield(root.right)
    return evaluate(root.val, x1,x2)


root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

            
