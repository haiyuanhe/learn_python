# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def FindPath(self, root, expectNumber):
        result = list()
        nums = list()

        def find_one_path(root, expectNumber):
            if root is None:
                return nums

            nums.append(root.val)
            expectNumber -= root.val
            if expectNumber == 0 and root.left is None and root.right is None:
                a = []
                a.extend(nums)
                result.append(a)
            find_one_path(root.left, expectNumber)
            find_one_path(root.right, expectNumber)
            nums.pop()
            return result

        return find_one_path(root, expectNumber)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.FindPath(root, 3)
