# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge(self, pHead1, pHead2):
        result = ListNode(1)
        p = result
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                result.next = pHead1
                pHead1 = pHead1.next
            else:
                result.next = pHead2
                pHead2 = pHead2.next
            result = result.next

        if pHead2:
            result.next = pHead2

        if pHead1:
            result.next = pHead1

        return p.next


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

    ll1 = ListNode(1)
    ll2 = ListNode(2)
    ll3 = ListNode(3)
    ll4 = ListNode(4)
    ll5 = ListNode(5)
    ll6 = ListNode(6)
    ll1.next = ll2
    ll2.next = ll3
    ll3.next = ll4
    ll4.next = ll5
    ll5.next = ll6

    p = s.merge(l1, ll1)
    while p != None:
        print p.val
        p = p.next
