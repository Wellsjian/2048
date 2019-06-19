"""
业务逻辑类  Business Logic Level(bll)
"""
"""
    逻辑处理模块
    1.0 将核心算法粘贴进来
    2.0 将所有参数，改为成员变量．
    3.0 在空白位置上随机产生新数字．
    4.0 如果地图有变化(数字移动／数字合并)
    5.0 判定游戏是否结束
"""

import random
import copy
from project_month01.my_2048_game.model import Victor
from project_month01.my_2048_game.model import Direction


class GameCoreController:
    """
    逻辑核心算法
    """

    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]
        # 存放0的列表
        self.__zero_map = []
        # 存放zero_to_end和merge的列表
        self.__new_map = []
        # self.__map = [
        #     [2,0,0,2],
        #     [2,4,0,2],
        #     [4,0,2,2],
        #     [2,2,0,2],
        # ]

    def zero_to_end(self):
        # 思路:删除0元素,再末尾增加.

        for i in range(len(self.__new_map) - 1, -1, -1):
            if self.__new_map[i] == 0:
                del self.__new_map[i]
                self.__new_map.append(0)

    def merge(self):
        self.zero_to_end()  # [2,0,0,2] -->  [2,2,0,0]
        # 如果相邻且相同

        for i in range(len(self.__new_map) - 1):
            if self.__new_map[i] == self.__new_map[i + 1]:
                # 合并[2,2,2,0] ->[4,2,2,0] --> [4,2,0,0]
                self.__new_map[i] += self.__new_map[i + 1]
                del self.__new_map[i + 1]
                self.__new_map.append(0)

        self.zero_to_end()

    def __move_left(self):
        # 思想:将每行(从左向右获取行数据)传递给合并函数
        for i in range(len(self.__map)):
            self.__new_map = self.__map[i][:]
            # 传递给merge函数的是二维列表中的元素(一维列表对象地址)
            # 函数都是操作对象,所以无需通过返回值拿到操作结果.
            self.merge()
            self.__map[i][:] = self.__new_map

    def __move_right(self):
        # 思想:将每行(从右向左获取行数据)传递给合并函数
        for i in range(len(self.__map)):
            # map[0][::-1] 从右向左获取行数据(新列表)
            self.__new_map = self.__map[i][::-1]
            self.merge()
            # 将合并后的结果,从右向左获还给二维列表
            self.__map[i][::-1] = self.__new_map

    def __move_up(self):
        for c in range(4):
            self.__new_map.clear()
            for r in range(4):
                self.__new_map.append(self.__map[r][c])
            self.merge()
            for r in range(4):
                self.__map[r][c] = self.__new_map[r]

    def __move_down(self):
        for c in range(4):
            self.__new_map.clear()
            for r in range(3, -1, -1):
                self.__new_map.append(self.__map[r][c])
            self.merge()
            # list_merge(从左到右) 赋值给 二维列表(从下到上)
            for r in range(3, -1, -1):  # 3 2 1 0
                self.__map[r][c] = self.__new_map[3 - r]

    def get_new_number(self):
        self.get_empty_postion()
        if len(self.__zero_map) == 0:
            return
        doc = random.choice(self.__zero_map)
        self.__map[doc.x][doc.y] = 4 if random.randint(1, 10) == 1 else 2
        self.__zero_map.clear()

    def get_empty_postion(self):
        for c in range(len(self.__map)):
            for r in range(len(self.__map)):
                if self.__map[c][r] == 0:
                    self.__zero_map.append(Victor(c, r))

    def move(self, dir):
        self.__map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.right:
            self.__move_right()
        self.print_map()

    def print_map(self):
        for c in self.__map:
            for r in c:
                print(r, end="   ")
            print()
