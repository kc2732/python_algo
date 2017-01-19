class Solution:
    def invertBinaryTree(self, root):
        if root:
            root.left, root.right = self.invertBinaryTree(root.right), self.invertBinaryTree(root.left)
        return root