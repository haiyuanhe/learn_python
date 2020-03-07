# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):

        i = 0
        j = len(array) - 1

        while i < j:
            if array[i] + array[j] > tsum:
                j = j - 1
            elif array[i] + array[j] < tsum:
                i = i + 1
            else:
                return [array[i], array[j]]

        return []


if __name__ == '__main__':
    s = Solution()
    print s.FindNumbersWithSum([1, 2, 3, 4, 5, 5, 6, 7, 8], 10)
