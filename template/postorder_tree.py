# -*- coding:utf-8 -*-
# https://www.acwing.com/blog/content/314/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_tree_recure(self, root):
        if root != None:
            self.postorder_tree_recure(root.left)
            self.postorder_tree_recure(root.right)
            print root.val

    # 左右根 是 根右左的逆序.
    def postorder_tree(self, root):
        result = []
        stack = []

        p = root
        while len(stack) >0 or p !=None:
            if p !=None:
                stack.append(p)
                result.append(p.val)
                p = p.right
            else:
                p = stack.pop()
                p = p.left

        return result[::-1]

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.postorder_tree_recure(root)
    print s.postorder_tree(root)
