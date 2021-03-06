"""
874. 模拟行走机器人

机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度

在网格上有一些格子被视为障碍物。
第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。

示例 1：
输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)

示例 2：
输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处

提示：
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
答案保证小于 2 ^ 31
"""


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        # current = [0, 0]
        # x, y = 0, 0
        # walkdirection = (0, 1)
        # maxway = 0
        # obstaclesset = set(map(tuple, obstacles))

        # def getdirection(d, r):
        #     if (d == (0, 1) and r == -1):
        #         return (1, 0)
        #     if (d == (0, 1) and r == -2):
        #         return (-1, 0)

        #     if (d == (1, 0) and r == -1):
        #         return (0, -1)
        #     if (d == (1, 0) and r == -2):
        #         return (0, 1)

        #     if (d == (0, -1) and r == -1):
        #         return (-1, 0)
        #     if (d == (0, -1) and r == -2):
        #         return (1, 0)

        #     if (d == (-1, 0) and r == -1):
        #         return (0, 1)
        #     if (d == (-1, 0) and r == -2):
        #         return (0, -1)

        # def movestep(x, y, s, d):
        #     for i in range(s):
        #         if ((x + d[0], y + d[1]) not in obstaclesset):
        #             x = x + d[0]
        #             y = y + d[1]
        #         else:
        #             break
        #     return x, y

        # for c in commands:
        #     if (c == -1 or c == -2):
        #         walkdirection = getdirection(walkdirection, c)
        #     else:
        #         x, y = movestep(x, y, c, walkdirection)
        #         maxway = max(maxway, (x * x + y * y))

        # return (maxway)

        obstacles_set = set(tuple(o) for o in obstacles)
        x, y = 0, 0
        d = 0
        faraway = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for c in commands:
            if (c == -1):
                d = (d + 1) % 4
            elif (c == -2):
                d = (d - 1) % 4
            else:
                movestep = directions[d]
                for i in range(c):
                    if ((x + movestep[0],
                         y + movestep[1]) not in obstacles_set):
                        x = x + movestep[0]
                        y = y + movestep[1]
                    else:
                        break
                faraway = max(faraway, (x * x + y * y))
        return(faraway)


s = Solution()

# print(s.robotSim([4, -1, 3], []))

# print(s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
a = [
    1, 2, -2, 5, -1, -2, -1, 8, 3, -1, 9, 4, -2, 3, 2, 4, 3, 9, 2, -1, -1, -2,
    1, 3, -2, 4, 1, 4, -1, 1, 9, -1, -2, 5, -1, 5, 5, -2, 6, 6, 7, 7, 2, 8, 9,
    -1, 7, 4, 6, 9, 9, 9, -1, 5, 1, 3, 3, -1, 5, 9, 7, 4, 8, -1, -2, 1, 3, 2,
    9, 3, -1, -2, 8, 8, 7, 5, -2, 6, 8, 4, 6, 2, 7, 2, -1, 7, -2, 3, 3, 2, -2,
    6, 9, 8, 1, -2, -1, 1, 4, 7
]
b = [[-57, -58], [-72, 91], [-55, 35], [-20, 29], [51, 70], [-61, 88], [
    -62, 99
], [52, 17], [-75, -32], [91, -22], [54, 33], [-45, -59], [47, -48], [53, -98],
     [-91, 83], [81, 12], [-34, -90], [-79, -82], [-15, -86], [-24, 66], [
         -35, 35
     ], [3, 31], [87, 93], [2, -19], [87, -93], [24, -10], [84, -53], [86, 87],
     [-88, -18], [-51, 89], [96, 66], [-77, -94], [-39, -1], [89, 51], [
         -23, -72
     ], [27, 24], [53, -80], [52, -33], [32, 4], [78, -55], [-25, 18], [
         -23, 47
     ], [79, -5], [-23, -22], [14, -25], [-11, 69], [63, 36], [35, -99], [
         -24, 82
     ], [-29, -98], [-50, -70], [72, 95], [80, 80], [-68, -40], [65, 70], [
         -92, 78
     ], [-45, -63], [1, 34], [81, 50], [14, 91], [-77, -54], [13, -88], [
         24, 37
     ], [-12, 59], [-48, -62], [57, -22], [-8, 85], [48, 71], [12, 1],
     [-20, 36], [-32, -14], [39, 46], [-41, 75], [13, -23], [98, 10], [
         -88, 64
     ], [50, 37], [-95, -32], [46, -91], [10, 79], [-11, 43], [-94, 98], [
         79, 42
     ], [51, 71], [4, -30], [2, 74], [4, 10], [61, 98], [57, 98], [46, 43], [
         -16, 72
     ], [53, -69], [54, -96], [22, 0], [-7, 92], [-69, 80], [68, -73], [
         -24, -92
     ], [-21, 82], [32, -1], [-6, 16], [15, -29], [70, -66], [-85, 80], [
         50, -3
     ], [6, 13], [-30, -98], [-30, 59], [-67, 40], [17, 72], [79, 82], [
         89, -100
     ], [2, 79], [-95, -46], [17, 68], [-46, 81], [-5, -57], [7, 58], [
         -42, 68
     ], [19, -95], [-17, -76], [81, -86], [79, 78], [-82, -67], [6, 0], [
         35, -16
     ], [98, 83], [-81, 100], [-11, 46], [-21, -38], [-30, -41], [86, 18], [
         -68, 6
     ], [80, 75], [-96, -44], [-19, 66], [21, 84], [-56, -64], [39, -15], [
         0, 45
     ], [-81, -54], [-66, -93], [-4, 2], [-42, -67], [-15, -33], [1, -32], [
         -74, -24
     ], [7, 18], [-62, 84], [19, 61], [39, 79], [60, -98], [-76, 45], [
         58, -98
     ], [33, 26], [-74, -95], [22, 30], [-68, -62], [-59, 4], [-62, 35], [
         -78, 80
     ], [-82, 54], [-42, 81], [56, -15], [32, -19], [34, 93], [57, -100], [
         -1, -87
     ], [68, -26], [18, 86], [-55, -19], [-68, -99], [-9, 47], [24, 94], [
         92, 97
     ], [5, 67], [97, -71], [63, -57], [-52, -14], [-86, -78], [-17, 92], [
         -61, -83
     ], [-84, -10], [20, 13], [-68, -47], [7, 28], [66, 89], [-41, -17], [
         -14, -46
     ], [-72, -91], [4, 52], [-17, -59], [-85, -46], [-94, -23], [-48, -3], [
         -64, -37
     ], [2, 26], [76, 88], [-8, -46], [-19, -68]]

print(s.robotSim(a, b))
"""
此题解法：此题并不复杂，但是需要写的比较精巧，用于保证效率。

* 定义初始位置x,y=0,0
* 机器人（起始方向是北）每次能够移动的可能[(0,1),(1,0),(0,-1),(-1,0)]
    （初始按照顺时针排列，北0东1南2西3），初始的direction=0
* 如果是顺时针转direction依次+1，然后%4，利用余数就得知落在哪个方向上。
* 如果是逆时针转direction依次-1，然后%4。
* 获取可移动的数值，计算x+direction[i][0]，y+direction[i][1]
* 判断未来落脚的点是否在obstacles里，如果不是，继续移动下一步。反之返回当前位置。
* 为了提高查询的效率，需要将obstacles的List转换成为set
* 每移动一步都计算一下当前点到(0,0)的距离，保存最大的即可。
"""
