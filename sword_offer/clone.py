# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 复杂链表的复制
# 链表
# 复制

# 解题思路：
# 1.遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
# 2.重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
# 3.拆分链表，将链表拆分为原链表和复制后的链表

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return pHead
        tmp = pHead
        while tmp:
            clone = RandomListNode(tmp.label)
            clone.next = tmp.next
            tmp.next = clone

            tmp = tmp.next.next

        tmp = pHead
        while tmp:
            if tmp.random != None:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        clone = pHead.next
        while pHead:
            if pHead.next != None:
                cloneNode = pHead.next
                pHead.next = cloneNode.next
                if cloneNode.next is None:
                    cloneNode.next = None
                else:
                    cloneNode.next = cloneNode.next.next
                pHead = pHead.next

        return clone


if __name__ == '__main__':
    s = Solution()

    l1 = RandomListNode(1)
    l2 = RandomListNode(2)
    l3 = RandomListNode(3)
    l4 = RandomListNode(4)
    l5 = RandomListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    l1.random = l4
    l2.random = l1
    l3.ramdom = l3
    print l1
    a = s.Clone(l1)
    print a
    while a != None:
        print a.label
        a = a.next
