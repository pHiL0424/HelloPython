
prompt = "I'll tell you it's even or odd."
prompt += "\nenter a number: "

active = True
while active:
    number = input(prompt)
    number = int(number)
    if number == 0:
        active = False
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")

# while的使用，利用break退出循环。
prompt = "I'll tell you it's even or odd."
prompt += "\nenter a number: "
while True:
    number = input(prompt)
    number = int(number)
    if number == 0:
        print("0 is quit.")
        break
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")
