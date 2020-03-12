# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 根据前序遍历确定头结点.
    # 根据头结点确定 中序遍历中的  左右树
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            result = TreeNode(pre[0])
            # pre[0]是头结点
            result.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            #                                         这里上下是对应的.                这里上下是一一对应的.
            result.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return result


if __name__ == '__main__':
    s = Solution()
    s.reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
