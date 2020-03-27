# -*- coding:utf-8 -*-

# 把数组排成最小的数
# 最小 数


class Solution:
    # 思路一: 全部搞出来然后求最小.
    def PrintMinNumber(self, numbers):
        if len(numbers) < 1:
            return None
        result = set()
        self.permutation_char(numbers, 0, result)
        return min(result)

    def permutation_char(self, ss, i, result):
        if i == len(ss) - 1:
            result.add(int(''.join([str(x) for x in ss])))
        else:
            for j in range(i, len(ss)):
                ss[i], ss[j] = ss[j], ss[i]
                self.permutation_char(ss, i + 1, result)
                # 换回来保持原样
                ss[i], ss[j] = ss[j], ss[i]

    # 思路二: 进行排序. 排序的规则
    # 若ab > ba 则 a > b，
    # 若ab < ba 则 a < b，
    # 若ab = ba 则 a = b；
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])


if __name__ == '__main__':
    s = Solution()
    print s.PrintMinNumber([1, 2, 3])
