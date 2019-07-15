# coding: utf-8
import json
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 简单做法. python 超时
        # ans = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         if height[i] > height[j]:
        #             ans = max(ans, (j - i) * height[j])
        #         else:
        #             ans = max(ans, (j - i) * height[i])
        #
        # return ans

        # 两边同时走 实现 o(n)
        i = 0
        j = len(height) - 1
        ans = 0
        while i < len(height) and i < j:
            if height[i] > height[j]:
                ans = max(ans, (j - i) * height[j])
                j = j - 1
            else:
                ans = max(ans, (j - i) * height[i])
                i = i + 1

        return ans


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            height = stringToIntegerList(line)

            ret = Solution().maxArea(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
