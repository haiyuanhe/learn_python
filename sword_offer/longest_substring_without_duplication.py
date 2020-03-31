# -*- coding:utf-8 -*-


# 最长不含重复字符的子字符串
# 连续最长 不重复字符串
# 双指针 + hashset


class Solution:
    def longest_substring_without_duplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        res = 0
        hash = set()
        while j < len(s):
            if s[j] in hash:
                hash.remove(s[i])
                i = i + 1
            else:
                hash.add(s[j])
                j = j + 1
            res = max(res, len(hash))
        return res


if __name__ == '__main__':
    s = Solution()
    print s.longest_substring_without_duplication("abcabcefg")
