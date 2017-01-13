# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root, sign = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            sign+=1;
            return max(self.maxDepth(root.left,sign),self.maxDepth(root.right,sign))
        else:
            return sign