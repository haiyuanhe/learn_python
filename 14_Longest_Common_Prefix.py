import json


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ans = None
        for s in strs:
            tmp = ""
            i = 0
            if ans is None:
                ans = s
                continue
            for i in range(min(len(ans), len(s))):
                if ans[i] == s[i]:
                    tmp = tmp + ans[i]
                else:
                    break
            ans = tmp
        return ans


def stringToStringArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            strs = stringToStringArray(line)

            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
