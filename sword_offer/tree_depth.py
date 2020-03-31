# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的深度
# 递归求最高

class Solution:
    def TreeDepth(self, pRoot, i=0):
        if pRoot is None:
            return i
        i = i + 1
        return max(self.TreeDepth(pRoot.left, i), self.TreeDepth(pRoot.right, i))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.TreeDepth(root, 0)
