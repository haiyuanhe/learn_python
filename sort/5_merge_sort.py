class Solution(object):
    def sort(self, nums):
        if len(nums) < 2:
            return nums
        middle = len(nums) / 2
        left = nums[0:middle]
        right = nums[middle::]
        return self.merge(self.sort(left), self.sort(right))

    def merge(self, arr1, arr2):
        result = list()
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        if i < len(arr1):
            result.extend(arr1[i::])
        if j < len(arr2):
            result.extend(arr2[j::])

        return result


if __name__ == '__main__':
    s = Solution()
    print s.sort([3, 1, 2, 3, 4, 5, 6])
