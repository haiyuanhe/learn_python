# -*- coding:utf-8 -*-

# 翻转单词顺序

class Solution:
    def ReverseSentence(self, s):
        # write code here
        str_arry = s.split(" ")
        return " ".join(str_arry[::-1])


if __name__ == '__main__':
    s = Solution()
    print s.ReverseSentence("I am a Student")
