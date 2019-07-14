class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur_row, down = 0, 0

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows-1:
                down ^= 1
            cur_row += 1 if down else -1

        return ''.join([row for row in rows])

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToInt(input):
    return int(input)

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
            numRows = stringToInt(line)

            ret = Solution().convert(s, numRows)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()