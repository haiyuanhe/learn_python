class Solution(object):
    def sort(self, nums):
        if len(nums) < 2:
            return nums
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.sort([3, 1, 2, 3, 4, 5, 6])
