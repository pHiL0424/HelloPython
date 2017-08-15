# input的使用，判断奇偶数。
number = input("enter a number,and tell you it's even or odd: ")
number = int(number)
if number % 2 ==0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")