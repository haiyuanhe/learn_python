# -*- coding:utf-8 -*-
class Solution:
    #需要找规律进行推导. 最后结果就是 2的阶层次数
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            return pow(2, number - 1)


if __name__ == '__main__':
    s = Solution()
    s.jumpFloorII(10)
