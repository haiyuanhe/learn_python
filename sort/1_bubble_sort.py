class Solution(object):
    def sort(self, nums):
        r = len(nums)
        for i in range(0, r):
            for j in range(0, r - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.sort([100, 3, 1, 2, 3, 4, 5, 6])
