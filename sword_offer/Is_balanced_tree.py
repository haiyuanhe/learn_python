# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 判断是否为平衡二叉树
# 深度差不超过一

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        return max(nLeft + 1, nRight + 1)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.IsBalanced_Solution(root)
