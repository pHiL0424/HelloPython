# 字典基础
person = {'firstname':'phil','lastname':'wang','age':33,'city':'sh'}
print(person)
print(person['firstname'].title()+ '.' + person['lastname'].title())

# 字典进阶
favlanguages = {
    'jen':'python',
    'tom':'c++',
    'sun':'java',
    'phil':'python',
}
print(favlanguages)
print(favlanguages['phil'])
favlanguages['phil'] = 'c#'
print(favlanguages['phil'])