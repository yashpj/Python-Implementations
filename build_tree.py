from collections import defaultdict , deque

# Tree Node class
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
    
    
def build_cookie_tree(descriptions):
    # diction : key -> chocolate_chip
    # value : reference : Node(chocolate_chip)
    root = None
    memory = defaultdict()
    
    for connection in descriptions:
        x,y,lr = connection[0],connection[1],connection[2]
        child = TreeNode(y)

        left = child if lr == 1 else None
        right = child if lr == 0 else None
        if x not in memory:
            node1 = TreeNode(x, left, right)
            memory[x] = node1
        else:
            node1 = memory[x]
            if lr ==1:
                node1.left = child
            else:
                node1.right = child

        memory[y] = child
        if root is None:
            root = memory[x]
    return root
    
    
    
descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))


