# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        a = list()
        a.append(root.val)
        self.print_tree(root, a)
        return a

    def print_tree(self, root, nums):
        if root != None:
            if root.left:
                nums.append(root.left.val)
            if root.right:
                nums.append(root.right.val)
            self.print_tree(root.left, nums)
            self.print_tree(root.right, nums)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.PrintFromTopToBottom(root)
