# 遍历字典
favlanguages = {
    'jen':'python',
    'tom':'c++',
    'sun':'java',
    'phil':'python',
}
print(favlanguages)
for name,language in favlanguages.items():
    print(name + ' like ' + language)

# 遍历字典的items/keys/values
lakes = {
    '鄱阳湖':'江西',
    '太湖':'江苏',
    '洞庭湖':'湖南',
    '纳木错':'西藏',
}
for lake,region in lakes.items():
    print(lake + ' in ' + region)
for lake in lakes.keys():
    print(lake)
for lake in sorted(lakes.keys()):
    print(lake)
for region in lakes.values():
    print(region)