# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversed_linked_list(self, pHead):
        p1 = pHead
        p2 = None
        while p1:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p2

    def list_length(self, p1):
        size = 0
        while p1:
            size = size + 1
            p1 = p1.next
        return size

    def reversed_linked_list_k(self, pHead, k):
        size = self.list_length(pHead)
        p1 = pHead
        p2 = None
        root = pHead
        tail = pHead

        for i in range(1, size % k):
            p1 = p1.next
            tail = tail.next

        p1 = p1.next
        count = 0
        while p1:
            if count < k:
                count = count + 1
                # 翻转
                tmp = p1.next
                p1.next = p2
                p2 = p1
                p1 = tmp
            else:
                count = 0
                tail.next = p2
                p2 = None
                while tail.next:
                    tail = tail.next

        tail.next = p2
        return root

    def reversed_linked_list_from_to(self, pHead, f, t):
        return pHead


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    pHead = s.reversed_linked_list_k(l1, 2)
    # pHead = s.reversed_linked_list(l1)
    while pHead:
        print pHead.val
        pHead = pHead.next

    # pHead = s.reversed_linked_list_from_to(l1, 0, 3)
    # while pHead:
    #     print pHead.val
    #     pHead = pHead.next
