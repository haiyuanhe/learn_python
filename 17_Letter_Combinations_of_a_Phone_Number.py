import json


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_map = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []
        for num in digits:
            ans = self.multiply(ans, dig_map[num])

        return ans

    def multiply(self, l1, l2):
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1

        m = []
        for i in l1:
            for j in l2:
                m.append("%s%s" % (i, j))
        return m


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            digits = stringToString(line)

            ret = Solution().letterCombinations(digits)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
