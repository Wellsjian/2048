




class Victor:
    a = 1
    @classmethod
    def play(cls):
        print(a)
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        self.__y = value

class Direction:
    up = 1
    down = 2
    right = 3
    left = 4

