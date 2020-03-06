# -*- coding:utf-8 -*-


class Solution:
    def Permutation(self, ss):
        if ss is None or len(ss) == 0:
            return []
        result = set()
        self.permutation_char([c for c in ss], 0, result)
        return sorted(list(result))

    def permutation_char(self, ss, i, result):
        if i == len(ss) - 1:
            result.add(''.join(ss))
        else:
            for j in range(i, len(ss)):
                ss[i], ss[j] = ss[j], ss[i]
                self.permutation_char(ss, i + 1, result)
                # 换回来保持原样
                ss[i], ss[j] = ss[j], ss[i]


if __name__ == '__main__':
    s = Solution()
    print s.Permutation("a")
    # s.Permutation("abccdd")
