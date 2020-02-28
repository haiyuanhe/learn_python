class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """



def stringToString(input):
    return input[1:-1].decode('string_escape')


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

            ret = Solution().longestPalindrome(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
