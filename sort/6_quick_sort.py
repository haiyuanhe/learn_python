class Solution(object):
    def sort(self, nums):
        return self.quick_sort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, l, r):
        if l < r:
            left, right = l - 1, r + 1
            tmpVal = nums[(l + r) // 2]
            while left < right:
                while True:
                    left += 1
                    if nums[left] >= tmpVal:
                        break
                while True:
                    right -= 1
                    if nums[right] <= tmpVal:
                        break
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            self.quicksort(nums, l, right)
            self.quicksort(nums, right + 1, r)

    def quick_sort3(self, list, left, right):
        if left < right:
            i = left - 1
            j = right + 1
            mid = list[(i + j) // 2]
            while i < j:
                while 1:
                    i += 1
                    if list[i] >= mid: break
                while 1:
                    j -= 1
                    if list[j] <= mid: break
                if i < j:
                    list[i], list[j] = list[j], list[i]

            self.quick_sort(list, left, j)
            self.quick_sort(list, j + 1, right)


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
    print s.quick_sort([4, 5, 1, 6, 2, 7, 2, 8], 0, len([4, 5, 1, 6, 2, 7, 2, 8]) - 1)
    a = [4, 5, 1, 6, 2, 7, 2, 8]
    s.quicksort(a, 0, len(a) - 1)
    print a
    a = [4, 5, 1, 6, 2, 7, 2, 8]
    s.quick_sort3(a, 0, len(a) - 1)
    print a
