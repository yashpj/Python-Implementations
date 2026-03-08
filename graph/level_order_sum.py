from collections import deque
class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelSum(self, root: TreeNode) -> List[int]:  # noqa: F821
        if not root:
            return []

        nodes = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            sum_ = 0

            for i in range(level_size):
                node = queue.popleft()
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            nodes.append(sum_)

        return nodes