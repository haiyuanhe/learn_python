# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        s = set()
        for i in array:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)


if __name__ == '__main__':
    s = Solution()
    print s.FindNumsAppearOnce([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8])
