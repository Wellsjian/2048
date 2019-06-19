"""
2048  游戏核心算法
"""
#1.定义函数，将列表中元素移动至末尾
# [2,0,2,0] -->[2,2,0,0]
#  [2,0,0,2] -->[2,2,0,0]
#  [2,4,0,2] -- >[2,4,2,0]
#方法一
def zero_to_end(list_target):
    for i in range(len(list_target)):
        for j in range(i+1,len(list_target)):
            if list_target[i] == 0:
                list_target[i], list_target[j]= list_target[j], list_target[i]


# list_target = [2,0,0,2]
# print(zero_to_end(list_target))
#方法二  删除0元素， 在末尾补0
# def zero_to_end(list_target):
#     for i in range(len(list_target)-1,-1,-1):
#         if list_target[i] == 0:
#             del list_target[i]
#             list_target.append(0)

# list_target = [2,0,0,2]
# zero_to_end(list_target)
# print(list_target)

#2.# [2,2,0,0] -->[4,2,0,0]
#  [2,0,0,2] -->[4,0,0,0]
#  [2,2,0,2] -- >[4,2,0,0]
#  [2,2,0,4] -- >[4,4,0,0]
# 方法一
def combine(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)


#方法二
def combine1(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)
list_target = [2,4,2,2]
# combine(list_target)
# print(list_target)
combine1(list_target)
print(list_target)




# 3.
#     [
#     [2,2,0,2]
#     [0,2,0,4]
#     [2,0,4,2]
#     [0,4,2,2]
#     ]
#
def move_left(map):
    # 思想：将每行二维列表的每个元素传递给函数
    #
    for i in range(len(map)):
        combine(map[i])

# map = [
#     [2,2,0,2],
#     [0,2,0,4],
#     [2,0,4,2],
#     [0,4,2,2]
#     ]
# move_left(map)
# print(map)

# 4.定义函数，向右移动
#
def move_right(map):
    for i in range(len(map)):
        list_target = map[i][::-1]

        combine(list_target)
        map[i][::-1] = list_target
# move_right(map)
# print(map)

#2.# [2,2,0,0] -->[4,2,0,0]
#  [2,0,0,2] -->[4,0,0,0]
#  [2,0,4,2] -- >[4,2,0,0]
# #  [0,4,2,2] -- >[4,4,0,0]
def move_up(map):

    for i in range(len(map)):
        list01 = []
        for j in range(len(map)):
            list01.append(map[j][i])
        combine1(list01)
        for k in range(len(list01)):

            map[k][i] = list01[k]

map= [
    [2,2,0,2],
    [0,2,0,4],
    [2,0,4,2],
    [0,4,2,2]
    ]
#
# move_up(map)
# print(map,end="")


def move_down(map):
    for j in range(len(map)):
        list = []
        for i in range(len(map)-1,-1,-1):
            list.append(map[i][j])
        combine1(list)
        for i in range(len(list)-1,-1,-1):
            map[i][j] = list[len(list)-1-i]

move_down(map)
print(map,end="")




































