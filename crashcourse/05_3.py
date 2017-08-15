# 用户判断
users = ['tom','phil','admin','jack','eric']
for user in users:
    if user == 'admin':
        print('oh,you are administrator.')
    else:
        print('you are good user.')

# 判断列表是否为空
users.clear()
if users:
    print('user is full.')
else:
    print('we are need user.')

# 列表、for循环、if示例
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')


