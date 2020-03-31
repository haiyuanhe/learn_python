# coding: utf-8

# 和为S的连续正数序列
# 双指针问题
# 单调性问题

class Solution(object):
    def find_continuous_sequence(self, sum):
        res = []
        left, right = 1, 2
        while right <= (sum + 1) // 2 and right > left:
            tmp = int(float(right + left) / 2 * (right - left + 1))
            if tmp == sum:
                right += 1
                res.append([index for index in range(left, right)])
            elif tmp < sum:
                right += 1
            else:
                left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.find_continuous_sequence(15)
