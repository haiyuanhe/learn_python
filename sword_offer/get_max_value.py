# 礼物的最大价值
# 二维数组中 路径, 最大值
# 动态规划问题

class Solution(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        f = []
        for _ in range(m):
            f.append([0] * n)

        # 初始化第一行和第一列 要不然就全部都是 0
        f[0][0] = grid[0][0]
        for i in range(1, n):
            f[0][i] = f[0][i - 1] + grid[0][i]
        for j in range(1, m):
            f[j][0] = f[j - 1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + grid[i][j]

        return f[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.getMaxValue([[1, 2, 3, 4, 5, 6],
                         [7, 8, 9, 10, 11, 12],
                         [13, 14, 15, 16, 17, 18]])
