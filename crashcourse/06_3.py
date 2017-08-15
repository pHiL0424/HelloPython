# 字典列表
aliens = []
for alien in range(10):
    newalien = {'color':'green','point':5,'speed':'fast'}
    aliens.append(newalien)
for alien in aliens:
    print(alien)

# 字典存储列表
favlanguages = {
    'jen':['python','c','sql'],
    'tom':['c++','c'],
    'sun':['java','go'],
    'phil':['python'],
}
print(favlanguages)
for name,languages in favlanguages.items():
    print('\n' +name + ' like: ')
    for language in languages:
        print(language)
