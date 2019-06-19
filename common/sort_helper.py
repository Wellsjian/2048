class sort:
    """
    排序几种方法
    """

    # 冒泡排序
    def bubble(self,list_target):
        # 外层循环计算比较的轮数
        for i in range(len(list_target) - 1):
            # 内层循环把控计较次数
            for j in range(len(list_target) - 1 - i):
                if list_target[j] > list_target[j + 1]:
                    list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]

    # 选择排序
    def select(self,list_target):
        # 外层循环计算比较的轮数
        for i in range(len(list_target) - 1):
            min = i  # 假设list[i]为最小值
            # 内层循环把控计较次数
            for j in range(i + 1, len(list_target)):
                if list_target[min] > list_target[j]:
                    min = j
            # 如果i不是最小值就交换
            if min != i:
                list_target[min], list_target[i] = list_target[i], list_target[min]

    # 插入排序
    def insert(self,list_target):
        for i in range(1, len(list_target)):
            x = list_target[i]
            j = i - 1
            while j >= 0 and list_target[j] > x:
                list_target[j + 1] = list_target[j]
                j -= 1
            list_target[j + 1] = x

    # 完成一轮排序过程
    def sub_sort(self,list_target, low, high):
        # 基准数
        x = list_target[low]
        while low < high:

            while list_target[high] >= x and high > low:
                high -= 1
            list_target[low] = list_target[high]

            while list_target[low] < x and low < high:
                low += 1
            list_target[high] = list_target[low]
        # 将基准数插入
        list_target[low] = x
        return low

    # 快速排序
    # low表示第一个序列号，high是最后一个序列号
    def quick(self, list_target, low, high):
        if low < high:
            key = self.sub_sort(list_target, low, high)
            self.quick(list_target, low, key - 1)
            self.quick(list_target, key + 1, high)

    #二分法查找元素
    def search(self,list_targrt, key):

        low, high = 0, len(list_targrt) - 1

        while low <= high:
            middle = (low + high) // 2
            if list_targrt[middle] < key:
                low = middle + 1
            elif list_targrt[middle] > key:
                high = middle - 1
            else:
                return middle