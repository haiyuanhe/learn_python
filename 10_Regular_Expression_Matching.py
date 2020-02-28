class Solution(object):
    #Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print 1

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
            line = lines.next()
            p = stringToString(line)

            ret = Solution().isMatch(s, p)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()