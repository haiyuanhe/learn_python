class Solution(object):
    def sort(self, nums):
        gap = len(nums) / 2
        while gap > 0:
            for i in range(gap, len(nums)):
                for j in range(gap, i + 1):
                    if nums[j] < nums[j - gap]:
                        nums[j], nums[j - gap] = nums[j - gap], nums[j]
            gap = gap / 2
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.sort([1, 2, 3, 4, 5, 6, 100, 2, 4, 5, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8])
