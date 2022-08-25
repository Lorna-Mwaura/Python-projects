# calculator application
print("welcome to our calculator")
print('*'*40)
print('''Choose operation
1.Addition
2.Subtraction
3.Multiplication
4.Division
''')
operation =int(input())
print(operation)

if operation <=4:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if operation == 1:
        print(float(num1) + float(num2))
    elif operation == 2:
        print(float(num1) - float(num2))
    elif operation == 3:
        print(float(num1) * float(num2))
    elif operation == 4:
        print(float(num1) / float(num2))
else:
    print("Choose valid operation")
