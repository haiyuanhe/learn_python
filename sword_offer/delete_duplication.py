# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        result = ListNode(0)
        res = result
        result.next = pHead
        tmp = pHead
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
            else:
                res.next = tmp
                res = res.next
            tmp = tmp.next
        res.next = tmp
        return result.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l5 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    s = Solution()
    a = s.deleteDuplication(l1)

    while a:
        print a.val
        a = a.next
