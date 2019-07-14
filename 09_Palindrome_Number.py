class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Now let's think about how to revert the last half of the number. For number 1221,
        # if we do 1221 % 10, we get the last digit 1, to get the second to the last digit,
        # we need to remove the last digit from 1221, we could do so by dividing it by 10, 1221 / 10 = 122.
        # Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2,
        # and if we multiply the last digit by 10 and add the second last digit, 1 * 10 + 2 = 12,
        # it gives us the reverted number we want.
        # Continuing this process would give us the reverted number with more digits.

        #1. 简单的思路就是吧这个数字除一遍 .然后跟构造出来的数值跟自己一样就完事了.
        #2. 其他思路就是把他当字符串想.
        if x < 0:
            return False
        else:
            return x == int(str(x)[::-1])


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
            x = stringToInt(line)

            ret = Solution().isPalindrome(x)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()