"""
学生管理系统
"""


class StudentModel:
    """
    数据模型----学生模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


class StudentModelController:
    """
    逻辑控制类
    """

    def __init__(self):
        self.__stu_list = []

    #
    @property
    def stu_list(self):
        # 列表返回地址， 列表中的元素还能被外部修改
        return self.__stu_list
        # 每次返回新列表，复制一份列表，占用内存
        # return self.__stu_list[:]

    def add_student(self, student_model):
        """
        添加学生
        :param student_model: 值得是添加的对象
        :return:
        """

        student_model.id = self.__generate()
        self.__stu_list.append(student_model)

    def __generate(self):
        return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1

    def remove_student(self, id):
        """
        删除学生对象
        :param id: 根据id删除学生
        :return: 是否删除成功
        """
        for item in self.stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    @property
    def modify_student(self):
        return self.__modify_student

    @modify_student.setter
    def modify_student(self,value):
        self.__modify_student = value

    def __modify_student(self, student_model):
        """
        修改学生对象
        :param student_model: 根据id修改学生
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == student_model.id:
                item.name = student_model.name

                return True
        return False

    def output_student_by_score(self):

        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):

                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], \
                                                                                   self.__stu_list[r]
        # self.stu_view = StudentManagerView()
        # self.stu_view.output_student(self.__stu_list.copy())
        return self.stu_list

class StudentManagerView:
    """
    学生管理器师徒
    """
    def __init__(self):
        self.__controller =  StudentModelController()


    def __displat_menu(self):
        """
        显示菜单
        :return:
        """

        menu = """
        1) 添加学生
        2) 显示学生
        3) 删除学生
        4) 修改学生
        5) 按照成绩生序显示
        """
        print(menu)

    def __select_menu_item(self):

        number = int(input("请输入您的选择"))
        if number == 1:
            self.__add_student()
        elif number == 2:
            self.output_student(self.__controller.stu_list)
        elif number == 3:
            self.__delete_student()
        elif number == 4:
            self.__modify_student()
        elif number == 5:
            self.output_student(self.__controller.output_student_by_score())


    def __modify_student(self):
        id = int(input("请再次您输入您的id"))
        name = input("请重新输入您的姓名：")
        age = int(input("请重新输入您的年龄："))
        score = int(input("请重新输入您的分数："))
        self.model = StudentModel(name, age, score,id)
        if self.__controller.modify_student(self.model):
            print("修改成功")
        else:
            print("修改失败")


    def __delete_student(self):
        id = int(input("请输入您的id:"))
        if self.__controller.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    # @property
    # def output_student(self):
    #     return self.__output_student
    # @output_student.setter
    # def output_student(self,value):
    #     self.__output_student = value
    def output_student(self,stu_list):
        for item in stu_list:
            print("编号：%d 姓名：%s 年龄：%d 分数：%d" % (item.id, item.name, item.age, item.score))

    def __add_student(self):
        name = input("请输入您的姓名：")
        age = int(input("请输入您的年龄："))
        score = int(input("请输入您的分数："))
        self.model = StudentModel(name,age,score)
        self.__controller.add_student(self.model)

    def main(self):
        while True:
            self.__displat_menu()
            self.__select_menu_item()


view = StudentManagerView()
view.main()









#
# controller.add_student(StudentModel("无畏先锋", 18, 92))
# controller.add_student(StudentModel("钢铁侠", 18, 92))
# controller.add_student(StudentModel("雷神", 18, 92))
# # controller.remove_student(1)
# r1 = controller.modify_student(StudentModel("绿巨人", 18, 92, 2))
# print(r1)
# for item in controller.stu_list:
#     print(item.id, item.name, item.age, item.score)
