# -*- coding:utf-8 -*-

# 数组中出现次数超过一半的数字
# 超过 一半


# 默认的方法是 o(n)
# 可以通过互相消耗的方式来做

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        num = numbers[0]
        count = 1
        for n in numbers:
            if n == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = n
                count = 1
        return num


if __name__ == '__main__':
    s = Solution()
    print s.MoreThanHalfNum_Solution([1, 2, 3, 3, 3])
