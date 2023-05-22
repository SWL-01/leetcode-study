# Definition for a binary tree node.
# Time complexity: O(n * m), as it depends on the size of both trees.
# Space complexity: O(n), as it depends on the maximum height of the root tree.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if not root:
            return False

        elif self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True

        # we haven't found the subRoot tree in the current root tree. if it is same tree, return true,
        # if not return false.
        else:
            return self.isSameTree(root, subRoot)

    # method to check if root and subRoot are the same trees.
    def isSameTree(self, root, subRoot):
        if root and subRoot:
            return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,
                                                                                                            subRoot.right)
        if root == subRoot:
            return True
        else:
            return False
