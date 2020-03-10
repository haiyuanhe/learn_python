# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp
        return num1


if __name__ == '__main__':
    s = Solution()
    print s.Add(1, 2)
