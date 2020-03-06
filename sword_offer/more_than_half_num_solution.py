# -*- coding:utf-8 -*-
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

        count = 0
        for n in numbers:
            if n == num:
                count += 1
        if count > len(numbers) / 2:
            return num
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print s.MoreThanHalfNum_Solution([1, 2, 3])
