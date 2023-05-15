# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            d = left_path + right_path
            self.diameter = max(d, self.diameter)
            return max(left_path, right_path) + 1
        dfs(root)
        return self.diameter
