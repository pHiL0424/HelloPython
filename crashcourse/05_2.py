# 简单
color = 'green'
if color == 'green':
    print('color is ' + 'green')
color = 'red'
if color == 'green':
    print('color is ' + 'green')

# if/else
color = 'green'
if color == 'green':
    print('5 point')
else:
    print('10 point')
color = 'red'
if color == 'green':
    print('5 point')
else:
    print('10 point')

# if/elif/else
age = 67
if age < 2:
    print('he is a baby.')
elif age <= 4:
    print('he is smaller.')
elif age <= 13:
    print('he is a boy.')
elif age < 65:
    print('he is a man')
elif age >= 65:
    print('he is a oldman')