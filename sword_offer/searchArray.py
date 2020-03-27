# coding: utf-8

# 二维数组
# 查找
class Solution(object):
    def search_array(self, nums, target):
        iMax = len(nums)
        jMax = len(nums[0]) - 1

        i = 0
        j = jMax
        while i < iMax and j > 0:
            if nums[i][j] > target:
                j = j - 1
            elif nums[i][j] < target:
                i = i + 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print s.search_array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ], 12)
