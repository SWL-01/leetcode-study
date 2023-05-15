# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Print the original tree
    print("Original tree:")
    print_tree(root)

    # Invert the tree
    solution = Solution()
    inverted_tree = solution.invertTree(root)

    # Print the inverted tree
    print("Inverted tree:")
    print_tree(inverted_tree)


def print_tree(root):
    if root is None:
        return None
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    main()