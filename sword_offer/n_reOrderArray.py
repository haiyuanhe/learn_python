# -*- coding:utf-8 -*-
# 调整数组顺序是奇数位于偶数的前面
# 奇数
# 偶数
class Solution(object):
    def re_order_array(self, array):
        if len(array) < 1:
            return array

        for i in range(len(array)):
            if array[i] % 2 == 0:
                j = i + 1
                while j < len(array):
                    tmp = array[j]
                    if tmp % 2 != 0:
                        array.pop(j)
                        array.insert(i, tmp)
                        break
                    else:
                        j = j + 1
                        continue
        return array

    def re_order_array2(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            while i <= j and array[i] % 2 == 1:
                i = i + 1
            while i <= j and array[j] % 2 == 0:
                j = j - 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        return array


if __name__ == '__main__':
    s = Solution()
    print s.re_order_array([1, 2, 3, 4, 5])
    print s.re_order_array2([1, 2, 3, 4, 5])
