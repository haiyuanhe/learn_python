# -*- coding:utf-8 -*-
# https://www.acwing.com/blog/content/314/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder_tree_recure(self, root):
        if root != None:
            print root.val
            self.preorder_tree_recure(root.left)
            self.preorder_tree_recure(root.right)

    def preorder_tree(self, root):
        result = []
        stack = []
        p = root

        while len(stack) > 0 or p != None:
            if p != None:
                stack.append(p)
                result.append(p.val)
                p = p.left
            else:
                t = stack.pop()
                p = t.right

        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.preorder_tree_recure(root)
    print s.preorder_tree(root)
