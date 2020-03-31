# -*- coding:utf-8 -*-

# 求1+2+…+n 不能用乘除法运运算
# 递归
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n <= 1:
            return n

        n = n - 1
        return n + self.Sum_Solution(n) + 1


if __name__ == '__main__':
    s = Solution()
    print s.Sum_Solution(0)
