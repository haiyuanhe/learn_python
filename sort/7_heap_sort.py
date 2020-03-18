class Solution(object):
    def down(self, nums, size, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        # if left < size and nums[left] < nums[largest]:
        if left < size and nums[left] > nums[largest]:
            largest = left
        # if right < size and nums[right] < nums[largest]:
        if right < size and nums[right] > nums[largest]:
            largest = right

        if largest != index:
            nums[largest], nums[index] = nums[index], nums[largest]
            self.down(nums, size, largest)

    def up(self, nums, index):
        father = index / 2
        if father >= 0 and nums[father] > nums[index]:
            nums[father], nums[index] = nums[index], nums[father]
            self.up(nums, father)

    def heap_sort(self, nums):
        size = len(nums)

        for i in reversed(range(size / 2)):
            self.down(nums, size, i)
        # print nums

        for i in reversed(range(size)):
            # print i
            nums[i], nums[0] = nums[0], nums[i]
            self.down(nums, i, 0)
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.heap_sort([1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 6])
