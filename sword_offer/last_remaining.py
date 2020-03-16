# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        p = range(0, n)

        while len(p) > 1:
            i = (m + i - 1) % len(p)
            p.pop(i)
        return p[0]


if __name__ == '__main__':
    s = Solution()
    print s.LastRemaining_Solution(6, 7)
