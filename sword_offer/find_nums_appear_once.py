# coding: utf-8

# 数组中只出现一次的两个数字
# 如果只有一个数字, 全部做一次抑或, 相同的消掉, 剩下一个就是不一样的.
# 如果有两个, 那么抑或出来的结果是  xor = x ^ y
# 接着用这个xor 中为 1 的位置来抑或处理, 因为因为 要不就是 x 有1  要不y 有1
# 最后就知道  x

class Solution(object):
    def find_nums_appear_once(self, nums):
        xor = 0
        # 得到 xor = x ^ y
        for i in nums:
            xor ^= i
        num1, num2 = 0, 0
        mask = 1
        # 记录第几位是 1
        while xor & mask == 0:
            mask <<= 1

        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


if __name__ == '__main__':
    s = Solution()
    print s.find_nums_appear_once([1, 2, 3, 3, 4, 4, 5, 5])
