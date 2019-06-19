# （二）界面视图模块
# 　　　创建游戏核心类对象
# 　　　调用核心类对象的生成数字方法


from project_month01.my_2048_game.bll import GameCoreController
from  project_month01.my_2048_game.model import Direction
class View:
    def __init__(self):
        self.__manager = GameCoreController()

    def start_game(self):

        self.__manager.get_new_number()
        self.__manager.get_new_number()
        # self.__manager.print_map()
        self.move_direction()

    def move_direction(self):

        try:
            dir = input("请输入移动方向(wasd):")
        except:
            raise ValueError("value is error")
        if dir == "w":
            self.__manager.move(Direction.up)
        if dir == "a":
            self.__manager.move(Direction.left)
        if dir == "s":
            self.__manager.move(Direction.down)
        if dir == "d":
            self.__manager.move(Direction.right)




