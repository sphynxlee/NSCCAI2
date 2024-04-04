from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class Solution:
    def diameter_of_binary_tree(self, root):
        # set a global variable to store the longest path
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # update the longest path
            self.diameter = max(self.diameter, left_height + right_height)

            # return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()

result = solution.diameter_of_binary_tree(root)
print("binary tree diameter:", result)
