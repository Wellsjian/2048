import time

# 1.获取当前时间戳
time01 = time.time()
print(time01)

# 2.获取时间元组
time02 = time.localtime()
print(time02)

# 3.时间元组转换为字符串格式
time03 = time.strftime("%y/%m/%d %H:%M:%S", time02)
print(time03)

# 4.字符串格式转化为时间元组
time04 = time.strptime("2019/5/21", "%Y/%m/%d")
print(time04)

# 5.时间元组转换为时间戳
time05 = time.mktime(time04)
print(time05)

#6.获取当前时间
time06 = time.ctime()
print(time06)
