# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 判断二叉搜索树的后序遍历序列
# 二叉树
# 后续遍历

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return True
        i = 0
        while sequence[i] < sequence[-1]:
            i = i + 1
        for j in sequence[i:-1]:
            if j < sequence[-1]:
                return False
        # 整体判断完最后一个跟之后, 再判断里面子树是不是满足的.
        return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST(sequence[i:-1])


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.VerifySquenceOfBST([1, 3, 2, 4, 5])
