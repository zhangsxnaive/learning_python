import sys


def fun(a, b):
    print('this is function')
    a = a * b
    print(a)
    print(b)
    print('a = %s' % a)


# print(sys.path)


def sale_car(price, color, is_second_hand=False, height=100):
    print(' price is %s\n color is %s\n is_second_hand is %s\n height is %d' % (price, color, is_second_hand, height))


# sale_car(2000, 'red')
AGE = 100
a = None


def fun2():
    global a
    a = 10
    return a + AGE


print(fun2())
print(a)
