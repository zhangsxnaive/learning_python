# 格式化代码
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# list
classmates = ['zhangsx', "zhangjq", "niuxs", "fujl", 'zhoujh', 'zhangyf', 'wusy', 'cuix']
num = len(classmates)
classmates.pop()

# tuple
classmates = ('zhangsx', 'zhangjq', 'niuxs', 'fujl')
print(classmates)

# if 条件判断
age = 22
if age > 24:
    print(classmates)

for a in classmates:
    print(a)
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
# height = input('请输入您的身高(m)')
# weight = input('请输入您的体重(kg)')
height = 1.75
weight = 80.5
Bmi = float(weight) / pow(float(height), 2)
print('%.2f' % Bmi, end='')
if Bmi < 18.5:
    print('过轻')
elif Bmi < 25:
    print('正常')
elif Bmi < 28:
    print('过重')
elif Bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# for 循环
L = ['zhangsx', 'zhangjq', 'zhangsw', 'zhangyf']
for x in L:
    print('Hello %s' % x)

# dict 字典
d = {'money': 100, 'haveTimes': 200, 'noTimes': 100}
print(dir(list))
