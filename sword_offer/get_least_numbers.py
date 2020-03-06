# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        self.quick_sort(tinput, 0, len(tinput) - 1, k)
        return sorted(tinput[:k])

    # def quick_sort(self, nums, left, right, k):
    #     i = self.partition(nums, left, right)
    #     if left < right:
    #         self.quick_sort(nums, left, i - 1, k)
    #         self.quick_sort(nums, i, right, k)
    #     return nums

    def quick_sort(self, nums, left, right, k):
        if left >= right:
            return nums
        i = self.partition(nums, left, right)

        if i - left >= k:
            self.quick_sort(nums, left, i - 1, k)
        else:
            self.quick_sort(nums, i, right, k -i)

    def partition(self, nums, left, right):
        pivot = left
        while left < right:
            while nums[left] < nums[pivot]:
                left += 1
            while nums[right] > nums[pivot]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

    # def quick_sort(self, nums, left, right, k):
    #     if left >= right:
    #         return
    #     i = left - 1
    #     j = right + 1
    #     x = nums[left + right >> 1]
    #     while i < j:
    #         i = i + 1
    #         while nums[i] < x:
    #             i = i + 1
    #         j = j - 1
    #         while nums[j] > x:
    #             j = j - 1
    #         if i < j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #
    #     # self.quick_sort(nums, left, j, 0)
    #     # self.quick_sort(nums, j + 1, right, 0)
    #
    #     if j - left + 1 >= k:
    #         self.quick_sort(nums, left, j, k)
    #     else:
    #         self.quick_sort(nums, j + 1, right, k - (j - left + 1))


# void quick_sort(int q[], int l, int r)
# {
# if (l >= r) return;
#
# int i = l - 1, j = r + 1, x = q[l + r >> 1];
# while (i < j)
#     {
#         do i ++ ; while (q[i] < x);
# do j -- ; while (q[j] > x);
# if (i < j) swap(q[i], q[j]);
# }
#
# quick_sort(q, l, j);
# quick_sort(q, j + 1, r);
# }


if __name__ == '__main__':
    s = Solution()
    print s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 2, 8], 2)
    print s.GetLeastNumbers_Solution([100, 1, 2, 3, 4, 5, 6, 6, 7, 8, 4, 5, 1, 6, 2, 7, 2, 8, 9, 8, 7, 6, 5], 7)
