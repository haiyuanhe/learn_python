# -*- coding:utf-8 -*-

# 栈的压入、弹出序列
# stack  栈
# 模拟一遍压入和弹出

class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False

        stack = []
        for num in pushV:
            stack.append(num)
            # stack[-1] 栈顶
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
