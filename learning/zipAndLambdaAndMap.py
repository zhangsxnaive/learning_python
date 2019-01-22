a = [1, 2, 3]
b = [4, 5, 6]
zip(a, b)
print(zip(a, b))
print(list(zip(a, b)))

for i, j in zip(a, b):
    print(i / 2, j * 2)
