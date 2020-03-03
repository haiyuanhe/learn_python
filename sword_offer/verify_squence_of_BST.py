# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def VerifySquenceOfBST(self, sequence):
        size = len(sequence)
        if size == 0:
            return False
        i = 0
        while size:
            size -= 1
            while sequence[i] < sequence[size]:
                i += 1
            while sequence[i] > sequence[size]:
                i += 1

            if i < size:
                return False
            i = 0
        return True


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.VerifySquenceOfBST([1, 2, 3, 4, 5])
