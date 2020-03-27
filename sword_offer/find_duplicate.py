# -*- coding:utf-8 -*-

# 找出数组中重复数字
# 重复
class Solution(object):

    # 用额外空间 o(n) 时间复杂度是 o(1)
    # 排序O(nlogn) 空间复杂度 o(1)
    # 利用本身的特性, 把自己当成桶, 如果出现重复了就认为有重复. 否则就没有重复了.时间复杂度o(n), 空间复杂度 o(1)
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != nums[nums[i]]:
                # swap 这里出现了很多问题
                tmp = nums[i]
                tmp2 = nums[nums[i]]
                nums[i] = tmp2
                nums[tmp] = tmp

            if nums[i] != i and nums[i] == nums[nums[i]]:
                return nums[i]

    #抽屉原理：n+1 个苹果放在 n 个抽屉里，那么至少有一个抽屉中会放两个苹果。
    #如果取中间一半的抽屉, 那么打开看理论上都是 n/2 如果多了就是有问题了
    def findDuplicate2(self, nums):
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            count = 0

            #选取了其中一边
            for x in nums:
                if x >= left and x <= mid:
                    count = count + 1
            if count > mid - left + 1:
                right = mid
            else:
                left = mid + 1
        return right

if __name__ == '__main__':
    s = Solution()
    print s.findDuplicate([2, 3, 1, 0, 2, 5, 3])
    print s.findDuplicate2([2, 3, 5, 4, 3, 2, 6, 7])
