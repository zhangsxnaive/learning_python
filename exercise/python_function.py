# 关键字命名参数
from functools import reduce


def person(name, age, *, job=None, city=None):
    print(name, age, job, city)


person('zsx', 23, job='工程师', city='上海')


# 可变参数
def product(x, *num):
    s = x
    for i in num:
        s = s * i
    return s


print(product(2))


# 递归函数
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print(fact(3))

for i in 'zhangshuxin':
    print(i, end=' ')

testList = [12, 'Zhangshuxin', 'Apple', 'Orange', 23, 24, 'Banana']

testList = [s.lower() for s in testList if isinstance(s, str)]

print(testList)

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
names = ['adam', 'LISA', 'barT']


def normalize(name):
    return name[0].upper() + name[1:].lower()


names = map(normalize, names)

print(list(names))

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([1, 3, 4, 2]))

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
strNum = '123.456'

L = map(lambda x: DIGITS[x], [x for x in '123.456' if x in DIGITS])
print('123.456'.index('.'))


