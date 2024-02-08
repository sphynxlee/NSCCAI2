# binary tree and sum traversal

from typing import Optional

class Node:
        def __init__(self, value):
            self.value = value
            self.left: Optional['Node'] = None
            self.right: Optional['Node'] = None

# create a binary tree
def create_binary_tree():
    # create nodes
    root = Node(1)

    root.left = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)

    root.right = Node(9)
    root.right.right = Node(9)
    root.right.right.left = Node(5)

    return root

def binary_tree_traversal_sum(node: Optional[Node]):
    if node is None:
        return 0

    left_childNode = node.left
    right_childNode = node.right

    sum = node.value + binary_tree_traversal_sum(left_childNode) + binary_tree_traversal_sum(right_childNode)

    return sum


root = create_binary_tree()
print(binary_tree_traversal_sum(root))