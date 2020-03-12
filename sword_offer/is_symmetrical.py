# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
# 左子树的右子树和右子树的左子树相同即可，采用递归
# 非递归也可，采用栈或队列存取各级子树根节点

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def is_same(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False

        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and pRoot.right:
            return False
        return is_same(pRoot.left, pRoot.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d
    print s.isSymmetrical(root)
