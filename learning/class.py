class Calculator:
    name = 'Good Calculator'
    price = 18

    def __init__(self, name, price, width):
        self.name = name
        self.price = price
        self.w = width

    def add(self, x, y):
        result = x + y
        return result

    def minus(self, x, y):
        return x - y

    def times(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


# calculator = Calculator('张书新的计算器', 300, 20)

# print(calculator.name)
# print(calculator.price)
# print(calculator.add(32, 43))
# print(calculator.divide(12, 3))
# print(calculator.name, calculator.price, calculator.w)

a_in = input('请输入密码')  # input接收的是字符串
if a_in == '1':
    print('登陆成功！')
else:
    print('请输入正确的密码！')
