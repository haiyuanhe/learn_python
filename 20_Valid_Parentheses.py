class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for str in s:
            stack.append(str)
            if self.compare(stack[-2:]):
                stack.pop()
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

    def compare(self, list):
        if len(list) != 2:
            return False
        if list[0] == "(":
            if list[1] == ")":
                return True

        if list[0] == "{":
            if list[1] == "}":
                return True

        if list[0] == "[":
            if list[1] == "]":
                return True
        return False


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

            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
