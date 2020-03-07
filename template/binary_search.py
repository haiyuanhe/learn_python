class Solution(object):

    # int bsearch_1(int l, int r)
    # {
    # while (l < r)
    #     {
    #         int mid = l + r >> 1;
    #     if (check(mid)) r = mid;
    #     else l = mid + 1;
    #     }
    #     return l;
    # }

    # def binary_search(self, l, r):
    #     while l < r:
    #         mid = l + r >> 1
    #         if check(mid):
    #             r = mid
    #         else:
    #             l = mid + 1
    #     return l

    def binary_search(self, array, target):
        l = 0
        r = len(array)

        while l < r:
            mid = l + r >> 1
            if array[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    s = Solution()
    print s.binary_search([1, 2, 3, 4, 5, 6], 3)
