class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        # binary tree left child
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursively(current_node.left, value)
        # right child
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursively(current_node.right, value)

# Traversal methods
# In-order traversal: left, root, right
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

def decode_msg(order):
    if order == 'in':
        inorder_traversal(binary_tree.root)
    elif order == 'pre':
        preorder_traversal(binary_tree.root)
    elif order == 'post':
        postorder_traversal(binary_tree.root)
    else:
        print("Invalid order. Please choose 'in', 'pre', or 'post'.")

# Create a binary tree and insert words
binary_tree = BinaryTree()
words = ['through', 'day', 'calm', 'vibrant', 'jumping', 'waters', 'energizes', 'reflecting', 'sunlight', 'A', 'keenly', 'ponds', 'frogs', 'near', 'quietly', 'opulent']
for word in words:
    binary_tree.insert(word)



# Secret message that will be displayed properly with the correct order
secret_message = "The quick brown fox jumps over the lazy dog."

# Example usage
print("In-order traversal:")
decode_msg('in')
print("\n\nPre-order traversal:")
decode_msg('pre')
print("\n\nPost-order traversal:")
decode_msg('post')
