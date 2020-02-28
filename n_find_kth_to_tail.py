class Solution(object):
    def FindKthToTail(self, array):
        if len(array) < 1:
            return array

        for i in range(len(array)):
            if array[i] % 2 == 0:
                j = i + 1
                while j < len(array):
                    tmp = array[j]
                    if tmp % 2 != 0:
                        array.pop(j)
                        array.insert(i, tmp)
                        break
                    else:
                        j = j + 1
                        continue

        return array


if __name__ == '__main__':
    s = Solution()
    print s.FindKthToTail([1, 2, 3, 4, 5])
