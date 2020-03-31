# coding: utf-8
# 有序数组中数值和下标相等的元素
# 有序数组  下标 = 值
# 二分对比, 看单调性

class Solution(object):
    def get_number_same_as_index(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] - mid >= 0:
                right = mid
            else:
                left = mid + 1  # 注意

        if nums[right] != right:
            right = -1
        return right


if __name__ == '__main__':
    s = Solution()
    print s.get_number_same_as_index([-3, -1, 1, 3, 5])