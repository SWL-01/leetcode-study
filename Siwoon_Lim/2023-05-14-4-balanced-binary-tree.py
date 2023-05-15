# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.height = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return left_balanced and right_balanced

    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
