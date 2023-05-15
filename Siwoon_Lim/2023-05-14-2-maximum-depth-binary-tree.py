# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return 0 value if there is no nodes in tree
        if root is None:
            return 0
        # add parent node as 1
        # max(value1, value2) -> return the largest value between value1 and value2
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Print the original tree
    print("Original tree:")
    print_tree(root)

    # use maxDepth to get the number of depth
    solution = Solution()
    dfs_tree = solution.maxDepth(root)
    print("# of dfs tree:")
    print(dfs_tree)


def print_tree(root):
    if root is None:
        return None
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    main()
