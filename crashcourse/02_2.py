
# 字符串的大小写处理
name = 'phil'
print('hi! ' + name)
print(name.title())
print(name.upper())
print(name.lower())

# 字符串拼接
famousperson = 'Albert Einstein'
x = '"A person who never made a mistake never tried anything new."'
print(famousperson + ' : ' + x)

# 剔除空白（空格/换行符/制表符等）
name = '\n\tAlbert Einstein '
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())