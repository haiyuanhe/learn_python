# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表有环
# 快慢指针

class Solution:
    def EntryNodeOfLoop(self, pHead):
        p1 = pHead
        p2 = pHead

        while p2 is not None and p2.next is not None:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                break

        if p2 is None or p2.next is None:
            return None

        p3 = pHead
        while p3 != p2:
            p2 = p2.next
            p3 = p3.next

        return p3


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l3

    s = Solution()
    print s.EntryNodeOfLoop(l1).val
