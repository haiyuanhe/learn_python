# -*- coding:utf-8 -*-

# 把数字翻译成字符串
# 0翻译成”a”，1翻译成”b”，……，11翻译成”l”，……，25翻译成”z”。
# 12258 ”bccfi”、”bwfi”、”bczi”、”mcfi”和”mzi”

class Solution:
    def getTranslationCount(self, s):
        if not s:
            return ''
        self.n = 0
        self.dfs(s)
        return self.n

    def dfs(self, s):
        if len(s) == 0:
            self.n += 1
            return
        else:
            # 两位的翻译方法
            if len(s) >= 2 and (int(s[:2]) <= 25 and s[0] != '0'):
                self.dfs(s[2:])
            # 一位的翻译方法
            if len(s):
                self.dfs(s[1:])


if __name__ == '__main__':
    s = Solution()
    print s.getTranslationCount("12258")
