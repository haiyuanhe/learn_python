# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树中和为某一值的路径
# 二叉树 数字和 路径

# 先序遍历, 同时将数值 变化, 记得要恢复现场.
class Solution:
    result = []

    def find_path(self, root, sum):
        path = []
        self.dfs(root, sum, path)
        return self.result

    def dfs(self, root, sum, path):
        if root is None:
            return
        path.append(root.val)
        sum = sum - root.val
        # 到叶子节点才算
        if sum == 0 and root.left is None and root.right is None:
            tmp = []
            tmp.extend(path)
            self.result.append(tmp)
        self.dfs(root.left, sum, path)
        self.dfs(root.right, sum, path)
        sum = sum + root.val
        path.pop()


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.find_path(root, 5)
