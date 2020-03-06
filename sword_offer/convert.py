# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None
        p = pRootOfTree
        stack = []
        is_first = True
        pre = None
        while p != None or len(stack) != 0:
            while p != None:
                stack.append(p)
                p = p.left

            p = stack.pop()
            if is_first:
                root = p
                pre = root
                is_first = False
            else:
                pre.right = p
                p.left = pre
                pre = p

            p = p.right
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    a = s.Convert(root)
    while a != None:
        print a.val
        a = a.right
