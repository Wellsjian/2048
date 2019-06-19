

class ListHelper:
    """
    列表助手：定义列表的常用操作
    """

    @staticmethod
    def find(list, func):
        """
        在列表中根据指定条件查找所有元素
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回生成器对象
        """
        for item in list:
            if func(item):
                yield item

    @staticmethod
    def first(list, func):
        """
        在列表中根据指定条件查找第一个元素
        :param list: 查找列表
        :param func: 指定条件
        :return: 满足条件的用第一个元素
        """
        for item in list:
            if func(item):
                return item

    @staticmethod
    def count(list, func):
        """
        在列表中根据指定条件查找某个元素出现的次数
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回数量
        """
        count = 0
        for item in list:
            if func(item):
                count += 1
                # yield count
        return count

    @staticmethod
    def get_sum(list, func):
        """
        在列表中根据指定条件查找某个元素出现的次数
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回数量
        """
        sum = 0
        for item in list:
               sum += func(item)
        return sum

    @staticmethod
    def get_max1(list,fun):
        """
        在列表中根据指定条件查找某个元素出现的次数
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回数量
        """
        max = fun(list[0])
        for item in list:
            if  max < fun(item):
                max = fun(item)
        return max

    # @staticmethod
    # def get_max2(list, fun):
    #     """
    #     在列表中根据指定条件查找某个元素出现的次数
    #     :param list: 查找列表
    #     :param func: 指定条件
    #     :return: 返回数量
    #     """
    #     max = list[0]
    #     for item in list:
    #         if fun(max) < fun(item):
    #             max =item
    #     return max

    @staticmethod
    def get_max(list, fun):
        """
        在列表中根据指定条件查找某个元素出现的次数
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回数量
        """
        max = list[0]
        for i in range(1,len(list)):
            if fun(max) < fun(list[i]):
                max = list[i]
        return max

    @staticmethod
    def get_element(list, fun):
        """
        在列表中根据指定条件查找某个元素出现的次数
        :param list: 查找列表
        :param func: 指定条件
        :return: 返回数量
        """
        list01 = []
        for item in list:
            list01.append(fun(item))

        return list01

    @staticmethod
    def order_by(list, fun):
        """
        根据条件对列表进行升序排列
        :param list: 查找列表
        :param func: 指定条件
        :return: 无返回值
        """

        for i in range( len(list) - 1):
            for j in range(i+1 , len(list) ):
                if fun(list[j]) > fun(list[i]):
                 list[j],list[i] = list[i],list[j]
        # return list











