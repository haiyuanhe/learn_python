# -*- coding:utf-8 -*-
class Solution:
    # 动态规划问题.
    # F[i] = max(F[i-1]+array[i], array[i])
    def FindGreatestSumOfSubArray(self, array):
        sum = list()
        sum.insert(0, array[0])
        for i in range(1, len(array)):
            sum.insert(i, max(sum[i - 1]+array[i], array[i]))
        return max(sum)


if __name__ == '__main__':
    s = Solution()
    print s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5])
    print s.FindGreatestSumOfSubArray([1, 2, 3, -1, -6, -6])
