class Solution(object):
    def sort(self, nums):
        for i in range(len(nums)):
            min = i
            for j in range(i + 1, len(nums)):
                if nums[min] > nums[j]:
                    min = j
            temp = nums[i]
            nums[i] = nums[min]
            nums[min] = temp
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.sort([3, 1, 2, 3, 4, 5, 6])
