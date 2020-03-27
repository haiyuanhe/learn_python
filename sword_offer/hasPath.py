# -*- coding:utf-8 -*-

# 矩阵中的路径
# 二维数组
# 路径
# dfs

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] == path[0]:
                    return self.dfs(matrix, i, j, path[1:])

    def dfs(self, matrix, i, j, path):
        if len(path) == 0:
            return True
        rows = len(matrix)
        cols = len(matrix[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        flag = False
        for index in range(4):
            i = i + dx[index]
            j = j + dy[index]
            if i >= 0 and i < rows and j >= 0 and j < cols and matrix[i][j] == path[0]:
                flag = True
                self.dfs(matrix, i, j, path[1:])

        return flag


if __name__ == '__main__':
    s = Solution()
    print s.hasPath([['a', 'b', 'c', 'd', 'e'],
                     ['f', 'i', 'j', 'k', 'l'],
                     ['n', 'm', 'o', 'p', 'q']
                     ], 3, 5, 'abcd')
