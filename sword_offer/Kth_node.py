# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    result = 0

    def KthNode(self, pRoot, k):
        self.inorder_tree_recure(pRoot, k)
        if self.result == 0:
            return None
        else:
            return self.result

    def inorder_tree_recure(self, root, k):
        if root != None:
            self.inorder_tree_recure(root.left, k)
            k = k - 1
            if k == 0:
                self.result = root.val
            self.inorder_tree_recure(root.right, k)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.KthNode(root, 3)
