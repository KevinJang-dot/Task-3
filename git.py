numbers = int(input("How many numbers you want to enter?"))
list_num =[]

for i in range(numbers):
    num = int(input("Enter num:"))
    list_num.append(num)

    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")
        list_num.append(num)

print(list_num)

for data in list_num:
    if data > 0:
        print(data, "This number is positive")
    elif data < 0:
        print(data, "This number is negative")
