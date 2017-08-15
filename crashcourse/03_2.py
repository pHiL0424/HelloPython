# 列表的顺序
place = ['chongqing','sanya','beijing','tianjing','luoyang']
print(place)
# sorted按字母排序，不改变原始列表
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)

# 反转列表顺序，改变原始列表
place.reverse()
print(place)
place.reverse()
print(place)

# 按字母排序，改变原始列表
place.sort()
print(place)
place.sort(reverse=True)
print(place)

# 列表长度
print(len(place))