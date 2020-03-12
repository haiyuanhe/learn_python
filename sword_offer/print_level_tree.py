# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # queue = []
        # # queue.pop(0)
        # # queue.append()
        # queue.append(pRoot)
        #
        # result = []
        # while len(queue):
        #     t = queue.pop(0)
        #     result.append(t.val)
        #     if t.left: queue.append(t.left)
        #     if t.right: queue.append(t.right)
        #
        # return result

        result = []
        if pRoot is None: return result
        queue = []
        queue.append(pRoot)
        while len(queue):
            low = 0
            size = len(queue)
            tmp = []
            while low < size:
                low = low + 1
                t = queue.pop(0)
                tmp.append(t.val)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
            result.append(tmp)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.Print(root)
