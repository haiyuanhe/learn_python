class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)


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
            N = stringToInt(line)

            ret = Solution().fib(N)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
