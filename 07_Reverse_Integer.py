class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            s = str(x)
            ans = int(s[::-1])
        else:
            x = x * -1
            s = str(x)
            ans = int(s[::-1]) * -1

        #边界问题需要注意
        if ans < pow(2, 31) - 1 and ans > pow(-2, 31):
            return ans
        else:
            return 0




def stringToInt(input):
    return int(input)


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
            x = stringToInt(line)

            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
