# -*- coding:utf-8 -*-
# 宽度搜索 可以找最短路. 边权都是1 可以用bfs


# 走迷宫
# 二叉树 层次遍历

# 模板
# 1. 初始队列
# 2. 判断队列是否为空
# 3. 弹出队头
# 4. 扩展队头

class Soluntion:
    def bfs(self, g):
        # 存储是否走过
        d = [[-1 for i in range(6)] for j in range(5)]
        # 用来判断上下左右 四个方向
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        # 初始队列
        queue = []

        queue.append([0, 0])
        # 走过了就标记为 0
        d[0][0] = 1

        while len(queue):
            # 弹出队头
            t = queue.pop(0)
            # 4个方向进行判断 , 可以走的进入队列里面去
            for i in range(0, 4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if x >= 0 and x < 5 and y >= 0 and y < 6 and d[x][y] == -1 and g[x][y] == 0:
                    # 标记走过的路的距离
                    d[x][y] = d[t[0]][t[1]] + 1
                    queue.append([x, y])

        return d


if __name__ == '__main__':
    s = Soluntion()
    d = [[0 for i in range(5)] for j in range(6)]
    g = [[0, 1, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0]]
    print s.bfs(g)
