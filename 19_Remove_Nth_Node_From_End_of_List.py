import json


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    count = 0
    max = 0
    count2 = 0

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        self.count = self.count + 1
        if head is None:
            self.max = self.count
            print self.max
            return
        self.removeNthFromEnd(head.next, n)

        if n != 0:
            if self.max != 0:
                self.count2 = self.count2 + 1
                if self.count2 == n + 1:
                    head.next = head.next.next
                    return head
                if self.max == n + 1:
                    return head.next

        return head


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


def stringToInt(input):
    return int(input)


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
            head = stringToListNode(line)
            line = lines.next()
            n = stringToInt(line)

            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
