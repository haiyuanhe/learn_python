# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 树的子结构
# 是否为子树

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        if self.is_subtree(pRoot1, pRoot2):
            return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                       pRoot2)

    def is_subtree(self, A, B):
        # B 已经判断完了
        if not B:
            return True
        # A还有, 但是A不等于B 的时候就返回false
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    lroot = TreeNode(2)
    lb = TreeNode(1)
    lc = TreeNode(3)
    lroot.left = lb
    lroot.right = lc

    print s.HasSubtree(root, lroot)
