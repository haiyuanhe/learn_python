# -*- coding:utf-8 -*-
# https://www.acwing.com/blog/content/314/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_tree_recure(self, root):
        if root != None:
            self.inorder_tree_recure(root.left)
            print root.val
            self.inorder_tree_recure(root.right)

    def inorder_traverse(self, root):
        result = []
        stack = []
        p = root

        while len(stack) > 0 or p != None:
            if p != None:
                stack.append(root)
                p = p.left
            else:
                p = stack.pop()
                result.append(p.val)
                p = p.right

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

    print s.inorder_traverse(root)
    print "\n"
    print s.inorder_tree_recure(root)
