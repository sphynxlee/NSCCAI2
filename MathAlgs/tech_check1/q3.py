class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursively(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursively(current_node.right, value)

def ascii_tree(node, level=0):
    if node != None:
        ascii_tree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        ascii_tree(node.right, level + 1)

# Create a binary tree and insert words
binary_tree = BinaryTree()
words = ['through', 'day', 'calm', 'vibrant', 'jumping', 'waters', 'energizes', 'reflecting', 'sunlight', 'A', 'keenly', 'ponds', 'frogs', 'near', 'quietly', 'opulent']
for word in words:
    binary_tree.insert(word)

# Function to print the binary tree in a tree-like structure

# Example usage
ascii_tree(binary_tree.root)
