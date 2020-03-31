# -*- coding:utf-8 -*-
# 滑动窗口的最大值

class Solution:
    def maxInWindows(self, num, size):
        result = []
        if size == 0:
            return []
        for i in range(0, len(num) - size + 1):
            result.append(max(num[i:i + size]))

        return result


if __name__ == '__main__':
    s = Solution()
    s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
