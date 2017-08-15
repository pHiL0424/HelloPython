# 访问列表
names = ['ren','yong','jun','fei']
print(names)
print(names[0] + ' come on!')
print(names[1] + ' come on!')
print(names[2] + ' come on!')
print(names[3] + ' come on!')

# 修改列表
names = []
names.append('yi')
names.append('wpy')
names.append('djj')
print(names)
print(names[-1] + ' is exit.')
names[-1] = 'wei'
print(names)
names.insert(0,'lhl')
names.insert(2,'wyj')
names.append('zdq')
print(names)
print('sorry,' + names.pop())
print('sorry,' + names.pop())
print('sorry,' + names.pop())
print('sorry,' + names.pop())
print(names)
del names[0]
print(names)
names.remove('yi')
print(names)
