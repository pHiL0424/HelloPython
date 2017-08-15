# 利用range函数生成1-20之间的数字
for value in range(1,21):
    print(value)

# 生成1-1000000之间的数字列表并统计
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 获取奇数列表
xnumbers = []
for value in range(1,21,2):
    xnumbers.append(value)
    print(value)
print(xnumbers)

# 获取被3整除的数字列表
ynumbers = []
for value in range(3,31,3):
    ynumbers.append(value)
    print(value)
print(ynumbers)

# 获取数字的立方列表
znumbers = []
for value in range(1,11):
    znumbers.append(value**3)
    print(value)
print(znumbers)

# 使用列表解析获取数字的立方列表
znumbers = [value**3 for value in range(1,11)]
print(znumbers)

# 切片
print('切片的使用…')
ns = znumbers[:]
print(ns)
print(ns[:3])
print(ns[3:6])
print(ns[-3:])


