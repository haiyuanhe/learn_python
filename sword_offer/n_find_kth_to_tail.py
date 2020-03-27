# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表中倒数第k个节点
# 链表
# kth

# 前后自增, 前面一个先走k 步, 然后
class Solution(object):
    def FindKthToTail(self, link, k):
        n = self.list_length(link)
        for i in range(n - k):
            link = link.next
        return link

    def list_length(self, p1):
        size = 0
        while p1:
            size = size + 1
            p1 = p1.next
        return size


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    print s.FindKthToTail(l1, 3).val
