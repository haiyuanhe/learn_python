# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次打印二叉树
# 层次 level
# 二叉树

class Solution:

    # 不分level 的做法
    def Print2(self, pRoot):
        queue = []
        queue.append(pRoot)
        result = []
        while len(queue):
            t = queue.pop(0)
            result.append(t.val)
            if t.left: queue.append(t.left)
            if t.right: queue.append(t.right)
        return result

    # 区分level 的做法
    # 同时 之字形打印
    def Print3(self, root):
        queue = []
        queue.append(root)
        level = 1
        while len(queue):
            tmp = []
            if level % 2:
                print [i.val for i in queue]
            else:
                print [i.val for i in reversed(queue)]

            while len(queue):
                t = queue.pop(0)
                if t.left:
                    tmp.append(t.left)
                if t.right:
                    tmp.append(t.right)

            if len(queue) == 0:
                queue = tmp
                level = level + 1

    # 区分level 的做法
    # def Print(self, pRoot):
    #     result = []
    #     if pRoot is None: return result
    #     queue = []
    #     queue.append(pRoot)
    #     while len(queue):
    #         low = 0
    #         size = len(queue)
    #         tmp = []
    #         while low < size:
    #             low = low + 1
    #             t = queue.pop(0)
    #             tmp.append(t.val)
    #             if t.left:
    #                 queue.append(t.left)
    #             if t.right:
    #                 queue.append(t.right)
    #         result.append(tmp)
    #     return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.Print2(root)
    print ""
    print s.Print3(root)
