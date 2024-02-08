from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

root = TreeNode("chased")
root.left = TreeNode("cat")
root.right = TreeNode("mouse")
root.left.left = TreeNode("The")
root.left.right = TreeNode("the")

def dfs_traversal(node: Optional[TreeNode], sentence: list):
    if node is not None:
        dfs_traversal(node.left, sentence)

        sentence.append(node.value)

        dfs_traversal(node.right, sentence)


# Perform depth-first search traversal
result_sentence = []
dfs_traversal(root, result_sentence)

# Output the sentence
output_sentence = ' '.join(result_sentence)
print(output_sentence)
