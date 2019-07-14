# coding: utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, str):
        # 1. 直接两个for loop  o(n^2)
        # max_num = 0
        # for i in range(len(str)):
        #     sub_string = set()
        #     sub_string.add(str[i])
        #     for j in range(i+1, len(str)):
        #         if str[j] in sub_string:
        #             if max_num < len(sub_string):
        #                 max_num = len(sub_string)
        #             break
        #         sub_string.add(str[j])
        #     else:
        #         if max_num < len(sub_string):
        #             max_num = len(sub_string)
        #
        #     if max_num + i > len(str):
        #         break
        # return max_num

        # 2. sliding window

        ans = 0
        i = 0
        j = 0
        sub_string = set()
        while i < len(str) and j < len(str):
            if str[j] not in sub_string:
                sub_string.add(str[j])
                j = j + 1
                ans = max(ans, len(sub_string))
            else:
                sub_string.remove(str[i])
                i = i + 1

        return ans



def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            s = stringToString(line)

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
