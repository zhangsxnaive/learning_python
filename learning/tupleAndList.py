# 元组是用括号定义
a_tuple = (1, 2, 3, 4, 5)
another_tuple = 1, 3, 4, 5, 6
a_list = [1, 2, 3, 4, 5, 1]

for content in a_list:
    print(content)

for content in a_tuple:
    print(content)

# append insert remove index count sort
a_list.append('append')
a_list.insert(0, 'zero')
# a_list.remove('zero')
a_list.remove(1)  # 先remove掉第一个查找到的值
a_list.index('append')
a_list.count(1)
# a_list.sort()  # 默认从小到大，并且列表会改变（纯数字）
# a_list.sort(reverse=True)  # 从大到小

print(a_list[-1])  # 最后一个是-1
print(a_list.index('append'))
print(a_list.count(1))
# for index in range(len(a_list)):
#     print('index is %s,value is %s' % (index, a_list[index]))

# 多维列表
multi_list = [
    ['a', 'b', 'c'],
    [1, 2, 3, 4],
    ['x', 'y', 'z']
]

print(multi_list[1])

