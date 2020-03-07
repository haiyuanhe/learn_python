# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        return s[n:len(s)]+s[0:n]

if __name__ == '__main__':
    s = Solution()
    print s.LeftRotateString("abcdefghijklmn", 3)