# coding: utf-8

import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 思路:
# 1. 数字转化链表
# 2. 10进制处理

# TODO
# 原始思路应该是进位 这个需要补充



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        i = 0
        while l1 is not None:
            num1 = num1 + l1.val * pow(10, i)
            i = i + 1
            l1 = l1.next

        num2 = 0
        i = 0
        while l2 is not None:
            num2 = num2 + l2.val * pow(10, i)
            i = i + 1
            l2 = l2.next

        # number to listnode
        dummyRoot = ListNode(0)
        for number in str(num1 + num2):
            cur = ListNode(number)
            cur.next = dummyRoot.next
            dummyRoot.next = cur

        return dummyRoot.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            print l1
            line = lines.next()
            l2 = stringToListNode(line)
            print l2

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
