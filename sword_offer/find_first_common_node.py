# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 两个链表的第一个公共结点
# p1 节点走a 走完之后走 p2 的长度 那么 p1 = a+b
# p2 节点走b 走完之后走 p1 的长度 那么 p2 = b+a
# 如果有公共节点那么就会出现 a+b = b+a

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = pHead2 if p1 == None else p1.next
            p2 = pHead1 if p2 == None else p2.next
        return p1


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    ll1 = ListNode(1)
    ll2 = ListNode(2)
    ll3 = ListNode(3)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    ll1.next = ll2
    ll2.next = ll3
    ll3.next = l3

    s = Solution()
    print s.FindFirstCommonNode(l1, ll1).val
