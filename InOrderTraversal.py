# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :Given a binary tree, return the inorder traversal of its nodes' values.
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        result = []
        while cur:
            if cur.left is None:
                result.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right != None and prev.right != cur:
                    prev = prev.right
                if prev.right == None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None;
                    result.append(cur.val)
                    cur = cur.right
        return result

    def inorderTraversalIterative(self,root):
        stack, result = [], []
        curNode = root

        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            result.append(curNode.val)
            curNode = curNode.right

        return result

    def inorderTraversalRecursive(self,root):
        result = []
        self.InOrT(root, result)
        return result

    def InOrT(self, root, result):
        if root:
            self.InOrT(root.left, result)
            result.append(root.val)
            self.InOrT(root.right, result)