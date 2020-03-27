# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#对称二叉树
#对称
#二叉树

# 思路：首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
# 左子树的右子树和右子树的左子树相同即可，采用递归


class Solution:
    def is_symmetrical_tree(self, pRoot):
        # write code here
        def is_same(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False

        if not pRoot:
            return True
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
    print s.is_symmetrical_tree(root)
