# -*- coding:utf-8 -*-
# 数值的整数次方
class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        result = 1.00
        for i in range(abs(exponent)):
            result = result * base
        if exponent < 0:
            return float(1 / result)

        return result


if __name__ == '__main__':
    s = Solution()
    print s.Power(10, 2)
    print s.Power(10, -3)
