class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return

def printTree(root):
    if root is None:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
    return

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

printTree(root)
invertBinaryTree(root)
printTree(root)