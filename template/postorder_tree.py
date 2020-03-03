# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_tree_recure(self, root):
        if root != None:
            self.inorder_tree_recure(root.left)
            self.inorder_tree_recure(root.right)
            print root.val

    def postorder_tree(self, root):
        stack = []
        node = root
        while len(stack) > 0 or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
            print node.val  # 访问node节点，如输出node的value

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)

    root.left = b
    root.right = c
    c.right = d

    print s.postorder_tree(root)
    print "\n"
    print s.postorder_tree_recure(root)