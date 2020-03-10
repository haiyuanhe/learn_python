# -*- coding:utf-8 -*-
import collections

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        flag = False
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                flag = True
                break
        return flag


if __name__ == '__main__':
    s = Solution
    s.duplicate([2, 3, 1, 0, 2, 5, 3], 2)

# https: // www.nowcoder.com / profile / 777988 / codeBookDetail?submissionId = 11041888
