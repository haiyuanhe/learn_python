class Solution(object):
    def sort(self, nums):
        return self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, left, right):
        i = self.partition(nums, left, right)
        if left < right:
            self.quick_sort(nums, left, i - 1)
            self.quick_sort(nums, i, right)
        return nums

    def partition(self, nums, left, right):
        pivot = left
        while left <= right:
            while nums[left] < nums[pivot]:
                left += 1
            while nums[right] > nums[pivot]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

    def quicksortBetter(self, arr):
        if len(arr) < 2:
            return arr
        pivot = arr[len(arr) / 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksortBetter(left) + middle + self.quicksortBetter(right)


if __name__ == '__main__':
    s = Solution()
    print s.quicksortBetter([1, 3, 1, 2, 3, 4, 5, 6])
