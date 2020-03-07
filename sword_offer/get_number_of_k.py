# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # 直接api
        # return data.count(k)

        # 二分寻找 (logn)
        return self.binary_search(data, k + 0.5) - self.binary_search(data, k - 0.5)

    def binary_search(self, array, target):
        l = 0
        r = len(array)

        while l < r:
            mid = l + r >> 1
            if array[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    s = Solution()
    print s.GetNumberOfK([1, 3, 3, 3, 3, 3, 4, 5], 2)
